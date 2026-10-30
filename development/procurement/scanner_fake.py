"""Private-network-only scanner simulator for disposable procurement runtime tests."""

import hashlib
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

MAX_BYTES = 16 * 1024 * 1024
MALWARE_SENTINEL = b"PROCUREMENT_TEST_MALWARE"


class ScannerHandler(BaseHTTPRequestHandler):
	server_version = "TAGProcurementScannerFake/1"

	def log_message(self, format, *args):
		# Never log upload content or request-specific values in the disposable fixture.
		return

	def _respond(self, status, payload):
		body = json.dumps(payload, separators=(",", ":")).encode()
		self.send_response(status)
		self.send_header("Content-Type", "application/json")
		self.send_header("Content-Length", str(len(body)))
		self.send_header("Cache-Control", "no-store")
		self.end_headers()
		self.wfile.write(body)

	def do_GET(self):
		if self.path == "/healthz":
			self._respond(200, {"status": "ok", "adapter": "synthetic"})
		else:
			self._respond(404, {"error": "not_found"})

	def do_POST(self):
		if self.path != "/scan":
			self._respond(404, {"error": "not_found"})
			return
		try:
			length = int(self.headers.get("Content-Length", "-1"))
		except ValueError:
			length = -1
		if not 0 <= length <= MAX_BYTES:
			self._respond(413, {"error": "size_limit"})
			return
		content = self.rfile.read(length)
		if len(content) != length:
			self._respond(400, {"error": "incomplete_body"})
			return
		self._respond(
			200,
			{
				"verdict": "infected" if content == MALWARE_SENTINEL else "clean",
				"sha256": hashlib.sha256(content).hexdigest(),
			},
		)


if __name__ == "__main__":
	ThreadingHTTPServer(("0.0.0.0", 8765), ScannerHandler).serve_forever()
