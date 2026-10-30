#!/usr/bin/env python3
"""Create or verify only the locked disposable procurement Bench and site."""

import json
import os
import subprocess
import sys
from pathlib import Path

RUNTIME = Path("/runtime")
LOCK = json.loads((RUNTIME / "runtime.lock.json").read_text())
BENCH = Path("/home/frappe/dev/frappe-bench")
SITE = LOCK["site"]
ENV = dict(os.environ)
ENV.update(
	{
		"GIT_CONFIG_COUNT": "3",
		"GIT_CONFIG_KEY_0": "safe.directory",
		"GIT_CONFIG_VALUE_0": "/source/frappe",
		"GIT_CONFIG_KEY_1": "safe.directory",
		"GIT_CONFIG_VALUE_1": "/source/erpnext",
		"GIT_CONFIG_KEY_2": "safe.directory",
		"GIT_CONFIG_VALUE_2": "/source/tag_procurement",
	}
)


def run(label, args, cwd=BENCH):
	print(label, flush=True)
	return subprocess.run(args, cwd=cwd, env=ENV, check=True, text=True)


def revision(path):
	return subprocess.run(
		["git", "-C", str(path), "rev-parse", "HEAD"],
		cwd=path,
		env=ENV,
		check=True,
		capture_output=True,
		text=True,
	).stdout.strip()


def verify_source(name):
	path = Path("/source") / name
	if not (path / ".git").exists():
		raise RuntimeError("Required source checkout is missing: %s" % name)
	if revision(path) != LOCK["sources"][name]:
		raise RuntimeError("Source revision mismatch for %s; no implicit update is allowed" % name)
	if subprocess.run(["git", "-C", str(path), "status", "--porcelain"], env=ENV, check=True, capture_output=True, text=True).stdout:
		raise RuntimeError("Locked source checkout has changes: %s" % name)


def secret(name):
	return (Path("/run/secrets") / name).read_text().strip()


def main():
	if os.getuid() == 0:
		raise RuntimeError("Bootstrap must run as the image's unprivileged frappe user")
	if sys.version_info[:3] != (3, 14, 8):
		raise RuntimeError("Python runtime does not match the locked 3.14.8 version")
	if not os.access(BENCH.parent, os.W_OK):
		raise RuntimeError("Bench volume is not writable; run volume-init first")
	if int(subprocess.run(["node", "--version"], check=True, capture_output=True, text=True).stdout.lstrip("v").split(".")[0]) != LOCK["runtime"]["node_major"]:
		raise RuntimeError("Node major version does not match runtime lock")
	for name in LOCK["sources"]:
		verify_source(name)
	if BENCH.exists() and not any(BENCH.iterdir()):
		BENCH.rmdir()
	if not BENCH.exists():
		run(
			"Initialise pinned Frappe Bench",
			[
				"bench", "init", "--python", sys.executable, "--frappe-path", "/source/frappe",
				"--frappe-branch", "version-16", "--skip-redis-config-generation", "--skip-assets", str(BENCH),
			],
			cwd=BENCH.parent,
		)
	if not (BENCH / "env/bin/python").exists():
		raise RuntimeError("Bench is incomplete; inspect existing volume before retrying")
	if revision(BENCH / "apps/frappe") != LOCK["sources"]["frappe"]:
		raise RuntimeError("Bench Frappe revision does not match runtime lock")
	run(
		"Ensure pinned Frappe package and dependencies are installed",
		[
			"uv", "pip", "install", "--quiet", "-e", str(BENCH / "apps/frappe"),
			"--python", str(BENCH / "env/bin/python"),
		],
	)
	if not (BENCH / "apps/erpnext").exists():
		run("Install locked ERPNext source", ["bench", "get-app", "--skip-assets", "erpnext", "/source/erpnext"])
	if revision(BENCH / "apps/erpnext") != LOCK["sources"]["erpnext"]:
		raise RuntimeError("Bench ERPNext revision does not match runtime lock")
	app = BENCH / "apps/tag_procurement"
	if not app.exists():
		run("Link the editable procurement source", ["bench", "get-app", "--skip-assets", "--soft-link", "tag_procurement", "/source/tag_procurement"])
	run("Refresh editable procurement package", ["uv", "pip", "install", "--quiet", "--no-deps", "-e", str(app), "--python", str(BENCH / "env/bin/python")])
	common = BENCH / "sites/common_site_config.json"
	config = json.loads(common.read_text()) if common.exists() else {}
	workers = dict(config.get("workers", {}))
	workers.update({
		"procurement": {"timeout": 300, "background_workers": 1},
		"procurement_io": {"timeout": 300, "background_workers": 1},
	})
	config.update({
		"db_host": "mariadb", "db_port": 3306,
		"redis_cache": "redis://redis-cache:6379", "redis_queue": "redis://redis-queue:6379",
		"redis_socketio": "redis://redis-queue:6379", "webserver_host": "web", "webserver_port": 8000,
		"socketio_port": LOCK["ports"]["realtime"], "default_site": SITE, "scheduler_tick_interval": 15,
		"workers": workers,
	})
	common.write_text(json.dumps(config, indent=1, sort_keys=True) + "\n")
	if not (BENCH / "sites" / SITE).is_dir():
		run("Create disposable procurement site", [
			"bench", "new-site", SITE, "--db-host", "mariadb", "--db-root-username", "root",
			"--db-root-password", secret("db_root"), "--admin-password", secret("site_admin"),
			"--mariadb-user-host-login-scope", "%", "--install-app", "erpnext",
		])
	installed = set(subprocess.run(["bench", "--site", SITE, "list-apps"], cwd=BENCH, env=ENV, check=True, capture_output=True, text=True).stdout.split())
	if "erpnext" not in installed:
		run("Install ERPNext", ["bench", "--site", SITE, "install-app", "erpnext"])
	if "tag_procurement" not in installed:
		run("Install TAG Procurement", ["bench", "--site", SITE, "install-app", "tag_procurement"])
	run("Enable developer mode on disposable site", ["bench", "--site", SITE, "set-config", "developer_mode", "1"])
	run("Enable test mode on disposable site", ["bench", "--site", SITE, "set-config", "allow_tests", "true"])
	run("Build TAG Procurement assets", ["bench", "build", "--app", "tag_procurement"])
	for iteration in (1, 2):
		run("Migrate disposable site %s/2" % iteration, ["bench", "--site", SITE, "migrate"])
	run("Enable disposable scheduler", ["bench", "--site", SITE, "enable-scheduler"])
	run("Check Bench health", ["bench", "doctor"])
	print("PASS: isolated procurement site initialized", flush=True)


if __name__ == "__main__":
	try:
		main()
	except (RuntimeError, subprocess.CalledProcessError) as exc:
		print(str(exc) if isinstance(exc, RuntimeError) else "Procurement bootstrap failed; inspect the command above", file=sys.stderr)
		sys.exit(1)
