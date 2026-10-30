#!/usr/bin/env python3
"""Control the isolated, image-locked TAG Procurement development stack."""

import json
import os
import secrets
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOCK = json.loads((ROOT / "runtime.lock.json").read_text())


def prepare_secrets():
	secret_dir = ROOT / ".local" / "secrets"
	secret_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
	(ROOT / ".local").chmod(0o700)
	secret_dir.chmod(0o700)
	for key in ("db_root", "site_admin"):
		path = secret_dir / key
		if not path.exists():
			fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o400)
			with os.fdopen(fd, "w") as stream:
				stream.write(secrets.token_urlsafe(36) + "\n")
			path.chmod(0o444)


def compose(*args):
	return subprocess.run(compose_command(*args), cwd=ROOT, env=compose_env(), check=True)


def compose_env():
	env = dict(os.environ, **LOCK["images"])
	env["WEB_PORT"] = str(LOCK["ports"]["web"])
	env["REALTIME_PORT"] = str(LOCK["ports"]["realtime"])
	return env


def compose_command(*args):
	return [
		"docker",
		"compose",
		"--project-name",
		LOCK["project"],
		"--file",
		str(ROOT / "compose.yaml"),
		*args,
	]


def verify():
	result = subprocess.run(
		compose_command("ps", "--status", "running", "--services"),
		cwd=ROOT,
		env=compose_env(),
		check=True,
		capture_output=True,
		text=True,
	)
	active = set(result.stdout.split())
	expected = {
		"mariadb",
		"redis-cache",
		"redis-queue",
		"scanner-fake",
		"web",
		"realtime",
		"scheduler",
		"worker",
		"procurement-worker",
		"procurement-io-worker",
	}
	missing = expected - active
	if missing:
		raise RuntimeError("Required disposable services are not running: " + ", ".join(sorted(missing)))
	compose("exec", "-T", "web", "env/bin/python", "/runtime/verify.py")


def main():
	if len(sys.argv) != 2 or sys.argv[1] not in {"config", "up", "bootstrap", "verify", "status", "stop"}:
		raise SystemExit("Usage: runtime.py {config|up|bootstrap|verify|status|stop}")
	prepare_secrets()
	action = sys.argv[1]
	if action == "config":
		compose("config", "--quiet")
	elif action == "up":
		compose("up", "-d", "--wait", "mariadb", "redis-cache", "redis-queue", "scanner-fake")
		compose("run", "--rm", "volume-init")
		compose("run", "--rm", "bootstrap")
		compose("up", "-d", "--wait", "web", "realtime", "scheduler", "worker", "procurement-worker", "procurement-io-worker")
		verify()
	elif action == "bootstrap":
		compose("run", "--rm", "bootstrap")
	elif action == "verify":
		verify()
	elif action == "status":
		compose("ps", "--all")
	elif action == "stop":
		compose("stop")


if __name__ == "__main__":
	try:
		main()
	except subprocess.CalledProcessError as exc:
		print("Runtime command failed with exit code %s." % exc.returncode, file=sys.stderr)
		sys.exit(exc.returncode)
