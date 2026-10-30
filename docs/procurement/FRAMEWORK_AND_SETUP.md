# Framework and development setup

Owner: PROC-R01, PROC-R29. These are future implementation procedures, not commands already executed. See [references](REFERENCES.md) for inspected source.

## Inspected baseline

On 27 October 2026 local source reports Frappe **16.53.0** at `e8d41dd006` and ERPNext **16.52.1** at `ade850bbd6`. Frappe's manifest requires Python `>=3.14,<3.15`; Node `>=24`; ERPNext requires Frappe `>=16.50.0,<17.0.0`. Initial qualification uses Python 3.14 and Node 24 with recorded patch versions/image digests. Declare compatible dependency bounds consistent with used APIs, without claiming all earlier revisions were tested.

The root contains separate source repositories and no verified Bench/site runtime. Container availability, installed applications, database, scheduler, workers, private storage and rendered theme remain unverified. A source checkout is not a production environment.

## Disposable environment procedure

1. Inspect the supplied frappe_docker development examples and the locally running reference app stack. Pin compatible runtime/database/Redis image digests and record exact source commits; do not reuse mutable `latest` image references as reproducibility evidence.
2. Complete [PROC-P0-003](tasks/P0-ENVIRONMENT-AND-BOOTSTRAP.md#proc-p0-003) first: scaffold the independent `tag_procurement` repository, version this handbook in its sole canonical location, and create the instruction bridge and app-owned runtime configuration.
3. Complete [PROC-P0-002](tasks/P0-ENVIRONMENT-AND-BOOTSTRAP.md#proc-p0-002): use that configuration to start isolated database/Redis volumes, mount framework forks read-only, initialise a disposable Bench using the locally supported `bench init --frappe-path` option (inspect `bench init --help` first), create an explicitly named site, and install ERPNext and `tag_procurement`. Never place the app inside payroll or ERPNext source or reuse the WhatsApp site/volumes.
4. Enable developer/test mode only on the disposable site. Configure `procurement` and `procurement_io` queues, scheduler and this revision's realtime process. Use the checkout's actual runtime entrypoints rather than assuming older websocket commands.
5. Build scoped assets; migrate twice; verify DB, Redis and worker diagnostics using synthetic queued work. Block unexpected external networking in automated tests.
6. Capture existing Buying Desk and website theme references before adding owned navigation. Verify route resolution from generated metadata rather than assuming legacy `/app` routing.

Future commands from the confirmed Bench root, after replacing placeholders with actual disposable identifiers:

```sh
bench --site <dev-site> install-app tag_procurement
bench --site <dev-site> set-config developer_mode 1
bench --site <dev-site> set-config allow_tests true
bench --site <dev-site> migrate
bench build --app tag_procurement
bench --site <dev-site> enable-scheduler
bench version
bench --site <dev-site> list-apps
bench --site <dev-site> doctor
bench --site <dev-site> run-tests --app tag_procurement
```

## Harness and time correctness

P0 establishes the app's declared lint/type/browser scripts and records their exact commands; none are claimed to exist now. Use a fake clock, fake mail/scanner adapters, deterministic policy fixtures and two-company/two-vendor users. Integration tests use actual supported database locking/constraints. Verify timestamp conversion between UTC domain values and Frappe storage at offset boundaries before relying on any deadline command.

Production uses an immutable built image, private storage, TLS, configured backups and independent workers; no developer mode or `bench start`. Follow [release operations](OPERATIONS_AND_RELEASE.md).
