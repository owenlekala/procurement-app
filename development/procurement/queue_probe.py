"""Disposable-only synthetic queue diagnostic, imported by isolated workers."""

import re

import frappe


def record(token: str, queue_name: str) -> None:
	if not frappe.conf.get("allow_tests") or queue_name not in {"procurement", "procurement_io"}:
		raise RuntimeError("Synthetic runtime probes require the disposable test site")
	if not re.fullmatch(r"[a-f0-9]{32}", token):
		raise ValueError("Invalid synthetic probe token")
	from frappe.utils.background_jobs import get_queue

	key = "procurement:runtime:queue-probe:" + token + ":" + queue_name
	get_queue(queue_name).connection.setex(key, 120, token)


def record_scheduler() -> None:
	if not frappe.conf.get("allow_tests"):
		raise RuntimeError("Synthetic scheduler probe requires the disposable test site")
	token = frappe.cache().get_value("procurement:runtime:scheduler-token", shared=True)
	if not isinstance(token, str) or not re.fullmatch(r"[a-f0-9]{32}", token):
		return
	from frappe.utils.background_jobs import get_queue

	key = "procurement:runtime:scheduler-result:" + token
	get_queue("default").connection.setex(key, 120, token)
