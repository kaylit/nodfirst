# Module: Backend service

> **⚠ NOT YET PROVEN.** This module has never been used on a real project. Its rules come from standard practice. `init` asks the human to confirm before using it, and the first project that uses it must review every rule and record corrections in `project/lessons.md`.

**Version:** 0.1
**Scope:** server-side software without its own UI: HTTP APIs (REST/JSON or similar), background jobs and workers, event-driven and messaging services. Language- and framework-neutral. If the project also has a browser UI, activate `web` too; if it serves a mobile or desktop client, activate that module too.
**State:** **not yet proven** on any project. Written from standard practice; the first real project must review it and record what it changes.

## Rules (in addition to the constitution)

**Contract**
- **B1 – The contract is written before the code.** Every endpoint, message or job has a contract in the spec or plan: inputs, outputs, status or result codes, error shape, limits, authentication, idempotency. For HTTP, an OpenAPI (or equivalent) description is a plan deliverable and tests check the code against it.
- **B2 – One error shape.** All errors use the same documented structure (stable machine code in English, human message, correlation identifier). No internal detail (stack traces, queries, hostnames) leaves the service (C6).
- **B3 – Compatibility.** Clients you do not control keep running old versions. The plan states the versioning scheme, which changes are breaking, how long old versions live, and how they are retired. A breaking change is a new version, never a silent edit.
- **B4 – Idempotency and repetition.** Every operation that changes state says what happens when it is sent twice (retry, double click, redelivery): safe by design, protected by an idempotency key, or explicitly not safe with the reason.
- **B5 – Lists are bounded.** Every list endpoint or query has a default and a maximum page size, a stable order, and a documented pagination method. Nothing returns "all".

**Security and data**
- **B6 – Trust nothing from outside (C6).** Authentication and authorization are enforced on the server for every operation, per object (not only per route). All input is validated against the contract; output is limited to what the caller may see. Baseline checklist: OWASP API Security Top 10. Secrets come from the environment or a secret store, never from the repository; each environment has its own.
- **B7 – Data changes are migrations.** Every schema change is a versioned, reviewed migration that can run on production data, states whether it is reversible, and is tested against a copy of realistic data. Changes that break running code are split in steps (add, backfill, switch, remove).
- **B8 – Transactions and consistency.** The plan states, for every operation that touches several records or systems, what must succeed together, what the isolation expectations are, and what happens on partial failure. Calls to other systems are never inside a database transaction without a decision record.
- **B9 – Backup and restore are tested.** Where data matters, the plan states what is backed up, how often, how long it is kept, and the restore has been **run once** before release. Retention and deletion follow the profile and the spec (GDPR where it applies).

**Resilience and operations**
- **B10 – Every outbound call has a timeout and a failure plan.** Timeouts, retries (which errors, how many, with what backoff and jitter), circuit breaking or load shedding, and what the caller receives when the dependency is down. No unbounded retries, no unbounded queues.
- **B11 – Observable by design.** Structured logs with a correlation identifier that follows a request across services and jobs; metrics for rate, errors and latency; a health check for liveness and one for readiness; alerts for the conditions the spec calls critical. Logs never contain secrets or personal data beyond what the profile allows.
- **B12 – Configuration and deployment.** All configuration is external and validated at start (the service refuses to start with a missing or invalid value). Releases are repeatable and have a rollback path; the migration order relative to the code release is stated.
- **B13 – Limits protect the service.** Rate limits, payload size limits and per-caller quotas are decided, with where their counters live when there are several instances.

**Background jobs and events (if present)**
- **B14 – Jobs assume at-least-once.** A job can run twice or be interrupted: handlers are idempotent, have a timeout, a bounded retry policy, a place for jobs that keep failing (dead-letter queue or equivalent), and an owner who is alerted. Schedules state their time zone and what happens when a run is missed.
- **B15 – Events are contracts too.** Each event has a name, a versioned schema, an owner, the guarantee given (ordering, delivery, duplicates), and a retention. Consumers tolerate unknown fields and duplicates; poison messages do not block the stream. Replay is either supported or explicitly not.

## Typical quality gates (copy into `project/profile.md`, Section 6)
1. Lint and format, 2. type check where the language has one, 3. unit tests, 4. integration tests against **real** infrastructure of the same kind as production (database, queue) started locally or in CI, 5. contract check against the OpenAPI or event schema, 6. migration check (apply on an empty database and on a snapshot; run the rollback if one is promised), 7. dependency and container audit with no known high-severity issue, 8. a smoke test of the built artifact: it starts, passes the readiness check and answers one request, 9. for releases: restore test (B9) and rollback rehearsal on a non-production environment.

## Checklists

**Specify.** Who calls the service (people, apps, other services) and how they are identified. For every operation: inputs with limits, outputs, errors, who may call it, what changes, what happens on repetition, expected volume and latency. What is stored, for how long, who can read it, how it is deleted. What happens when a dependency is down. What the service must never do. Audit needs (who did what, when). For jobs: trigger, frequency, duration, what a missed or failed run means to the user.

**Plan.** Architecture in one diagram or list (components, data stores, queues, external services) and the reason for each. Contracts (B1–B5). Data model and migrations (B7). Authentication and authorization model with a table of operations against roles. Transactions and failure handling (B8, B10). Observability and alerts (B11). Environments, configuration, secrets and deployment (B12). Capacity assumptions with numbers from the spec, not invented. How each mechanism is tested **with the same component as in production** (a different database or queue in test is a decision). Run costs where relevant.

**Tasks.** Order: runtime and tools check, scaffolding and configuration validation, CI, health checks and logging skeleton, data model and first migration, authentication, then one operation or job per task, each with its tests and its contract entry. Account creation, secrets, DNS and cloud consoles are "Requires human action" tasks placed before the first task that needs them. Release and rollback are tasks. A task never relies on infrastructure that a later task creates.

## Typical open decisions
Language and framework, API style, data store and hosting, authentication method and identity provider, queue or broker, deployment model and environments, observability stack, versioning scheme, rate-limit design, retention and deletion, backup schedule, CI, secrets storage, cost limits.

## Proven and not yet proven
- **Proven:** nothing yet. The generic parts (spec, plan, tasks, analyze, implement) are proven on the web and library modules.
- **Not yet proven:** all rules above, especially B7 (migrations), B9 (restore), B14 and B15 (jobs and events), and the integration-test gate against real infrastructure.
