#!/usr/bin/env python3
"""Verify the isolated procurement Bench from inside its disposable web container."""

import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid
from datetime import timedelta
from pathlib import Path

import frappe

RUNTIME = Path("/runtime")
LOCK = json.loads((RUNTIME / "runtime.lock.json").read_text())
SITE = LOCK["site"]
EXPECTED_APPS = {"frappe", "erpnext", "tag_procurement"}
QUEUES = ("procurement", "procurement_io")
failures: list[str] = []


def check(name, operation):
	try:
		operation()
		print("PASS: " + name, flush=True)
	except Exception as exc:
		failures.append(name)
		print("FAIL: %s (%s)" % (name, type(exc).__name__), flush=True)


def require(condition, message):
	if not condition:
		raise RuntimeError(message)


def verify_apps_and_revisions():
	installed = set(frappe.get_installed_apps())
	require(EXPECTED_APPS <= installed, "required applications are missing")
	require(frappe.get_conf().get("developer_mode") == 1, "developer mode is not enabled")
	require(frappe.get_conf().get("allow_tests") is True, "test mode is not enabled")
	require(".".join(map(str, sys.version_info[:3])) == LOCK["runtime"]["python"], "Python version differs from runtime lock")
	node = subprocess.run(["node", "--version"], check=True, capture_output=True, text=True).stdout.strip()
	require(int(node.lstrip("v").split(".")[0]) == LOCK["runtime"]["node_major"], "Node major version differs from runtime lock")
	app_path = Path(frappe.get_app_path("tag_procurement")).resolve()
	require(app_path.is_relative_to(Path("/source/tag_procurement").resolve()), "app is not using the editable source")
	for name, expected in LOCK["sources"].items():
		require(frappe.get_app_version(name) == LOCK["versions"][name], "%s application version differs from runtime lock" % name)
		path = Path("/source") / name
		result = subprocess.run(
			["git", "-c", "safe.directory=" + str(path), "-C", str(path), "rev-parse", "HEAD"],
			check=True,
			capture_output=True,
			text=True,
		)
		require(result.stdout.strip() == expected, "%s source revision differs from runtime lock" % name)


def verify_database_and_redis():
	from frappe.utils.background_jobs import get_queue

	frappe.db.sql("SELECT 1")
	for queue in ("short", "default", "long", *QUEUES):
		require(get_queue(queue).connection.ping(), "queue Redis ping failed")
	cache = frappe.cache()
	require(cache.ping(), "cache Redis ping failed")
	cache.set_value("procurement:runtime:cache-probe", "ok", expires_in_sec=30, shared=True)
	require(
		cache.get_value("procurement:runtime:cache-probe", shared=True, use_local_cache=False) == "ok",
		"cache probe did not round-trip through Redis",
	)
	cache.delete_value("procurement:runtime:cache-probe", shared=True)


def verify_scheduler():
	from frappe.utils.scheduler import is_scheduler_inactive
	from frappe.utils import now_datetime
	from frappe.utils.background_jobs import get_queue

	require(not frappe.conf.get("pause_scheduler"), "scheduler is paused in site configuration")
	require(not is_scheduler_inactive(verbose=False), "site scheduler is disabled")
	token = uuid.uuid4().hex
	method = "queue_probe.record_scheduler"
	require(not frappe.db.exists("Scheduled Job Type", {"method": method}), "scheduler probe name is already in use")
	cache = frappe.cache()
	cache.set_value("procurement:runtime:scheduler-token", token, expires_in_sec=180, shared=True)
	job = None
	key = "procurement:runtime:scheduler-result:" + token
	connection = get_queue("default").connection
	try:
		job = frappe.get_doc(
			{
				"doctype": "Scheduled Job Type",
				"method": method,
				"frequency": "Cron",
				"cron_format": "* * * * *",
				"last_execution": now_datetime() - timedelta(minutes=2),
				"stopped": 0,
				"create_log": 0,
			}
		).insert(ignore_permissions=True)
		frappe.db.commit()
		deadline = time.monotonic() + 120
		while time.monotonic() < deadline and connection.get(key) != token.encode():
			time.sleep(0.5)
		require(connection.get(key) == token.encode(), "scheduler did not execute its synthetic scheduled job")
	finally:
		cache.delete_value("procurement:runtime:scheduler-token", shared=True)
		connection.delete(key)
		if job and frappe.db.exists("Scheduled Job Type", job.name):
			frappe.delete_doc("Scheduled Job Type", job.name, ignore_permissions=True, force=True)
		frappe.db.commit()


def verify_private_storage():
	private = Path(frappe.get_site_path("private", "files"))
	public = Path(frappe.get_site_path("public", "files")).resolve()
	private.mkdir(parents=True, exist_ok=True)
	private_resolved = private.resolve()
	private_root = Path(frappe.get_site_path("private")).resolve()
	require(private_resolved != public and private_resolved.is_relative_to(private_root), "private files resolve outside the private site directory")
	probe = private / ("procurement-runtime-" + uuid.uuid4().hex + ".probe")
	probe.write_bytes(b"synthetic private-storage health probe")
	try:
		os.chmod(probe, 0o600)
		require(
			hashlib.sha256(probe.read_bytes()).digest()
			== hashlib.sha256(b"synthetic private-storage health probe").digest(),
			"private storage read-back failed",
		)
	finally:
		probe.unlink(missing_ok=True)


def request(url, *, data=None, timeout=5):
	headers = {"Content-Type": "application/octet-stream"} if data is not None else {}
	request = urllib.request.Request(url, data=data, headers=headers)
	deadline = time.monotonic() + 45
	while True:
		try:
			with urllib.request.urlopen(request, timeout=timeout) as response:
				return response.status, response.read(1024 * 1024)
		except urllib.error.URLError:
			if time.monotonic() >= deadline:
				raise
			time.sleep(0.5)


def verify_realtime():
	port = int(LOCK["ports"]["realtime"])
	status, body = request("http://realtime:%s/socket.io/?EIO=4&transport=polling&t=procurement-health" % port)
	require(status == 200 and body.startswith(b"0{"), "Socket.IO polling handshake failed")
	status, body = request("http://web:8000/api/method/ping")
	require(status == 200 and json.loads(body).get("message") == "pong", "Frappe web health endpoint failed")


def verify_scanner_fake():
	status, health_body = request("http://scanner-fake:8765/healthz")
	require(status == 200 and json.loads(health_body).get("status") == "ok", "scanner health endpoint failed")
	for payload, expected in (
		(b"synthetic clean procurement attachment", "clean"),
		(b"PROCUREMENT_TEST_MALWARE", "infected"),
	):
		status, body = request("http://scanner-fake:8765/scan", data=payload)
		result = json.loads(body)
		require(status == 200 and result.get("verdict") == expected, "scanner fake returned an unexpected verdict")


def verify_queue_workers():
	from frappe.utils.background_jobs import enqueue, get_queue

	token = uuid.uuid4().hex
	for queue in QUEUES:
		key = "procurement:runtime:queue-probe:" + token + ":" + queue
		connection = get_queue(queue).connection
		connection.delete(key)
		enqueue(
			"queue_probe.record",
			queue=queue,
			timeout=30,
			job_id="procurement-runtime-probe-" + token + "-" + queue,
			token=token,
			queue_name=queue,
		)
		deadline = time.monotonic() + 45
		while time.monotonic() < deadline and not connection.get(key):
			time.sleep(0.25)
		require(connection.get(key) == token.encode(), queue + " worker did not complete its synthetic job")
		connection.delete(key)


def main():
	frappe.init(site=SITE)
	frappe.connect()
	try:
		check("pinned applications, editable source and source revisions", verify_apps_and_revisions)
		check("database, Redis cache and configured queues", verify_database_and_redis)
		check("site scheduler enabled", verify_scheduler)
		check("private site file storage", verify_private_storage)
		check("Frappe web and realtime health", verify_realtime)
		check("local scanner fake clean/infected verdicts", verify_scanner_fake)
		check("dedicated procurement and procurement_io worker jobs", verify_queue_workers)
	finally:
		frappe.destroy()
	if failures:
		print("FAIL: runtime verification failed for %s check(s)" % len(failures), file=sys.stderr)
		sys.exit(1)
	print("PASS: isolated procurement runtime verified", flush=True)


if __name__ == "__main__":
	main()
