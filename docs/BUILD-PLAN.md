# Business Foundations Engine — Build Plan

**Status:** READY TO START
**Safety posture:** Read-only ingestion until controlled-write commissioning passes.

## Slice 0 — Reconcile and secure

- Eli rotates the two discovered exposed credentials; store only redacted incident receipts.
- Capture fresh signed Mac Studio and MacBook state.
- Reconcile existing PMPS memory, registry, verify, drift, Notion and Librarian jobs; nominate one writer per projection.
- Freeze the authority map, lifecycle, event names and PMPS filing projection as configuration v1.0.

**Exit:** no unresolved authority conflict or secret in source/fixtures.

## Slice 1 — Runnable control plane

- Scaffold using Google Agent Starter Pack conventions.
- Add pinned Compose services: Temporal, PostgreSQL, OPA, MCP Toolbox, API/worker, parser and OpenTelemetry.
- Add health checks; prohibit host/Docker/credential mounts.
- Implement schemas, correlation IDs, idempotency and append-only events.

**Exit:** a synthetic workflow pauses for approval, resumes and replays without duplicate writes.

## Slice 2 — Corpus ingestion

- Register the PMPS corpus manifest and Librarian adapter.
- Add read-only Drive/local adapters, ClamAV, SHA-256, Docling, Presidio and exceptions.
- Benchmark difficult samples with Document AI and NeMo Retriever.
- Store originals by pointer; parsed derivatives stay restricted and lifecycle-controlled.

**Exit:** controlled SOP, project record and restricted record pass golden tests with explicit coverage.

## Slice 3 — Business model and gaps

- Implement entities, processes, roles, authorities, claims, contradictions, obligations, risks, controls and gaps.
- Import PMPS memory vocabulary through an adapter; do not copy uncontrolled facts.
- Load versioned generic, Commonwealth and NSW control packs with source/effective-date metadata.
- Generate provisional capability, process, authority and control maps.

**Exit:** every displayed claim resolves to evidence; unsupported conclusions stay proposed.

## Slice 4 — Adaptive interview

- Generate a risk/information-gain dossier after ingestion.
- Run one AI-guided process-owner interview.
- Produce atomic `CONFIRM`, `EXTEND`, `CORRECT`, `CONTRADICT` and `UNKNOWN` claims.
- Require review of the summary before promotion.

**Exit:** corrections update current truth without deleting history; transcript stays restricted.

## Slice 5 — Draft, audit and agent handoff

- Consolidate candidates before drafting.
- Generate one controlled SOP and improvement programme.
- Generate tools, approvals, exceptions, monitoring and evaluation cases as an agent specification.
- Run provenance audit, OPA tests, ADK eval and garak.

**Exit:** exact hash approved, Drive write read back, lifecycle replayed and agent specification passes.

## Slice 6 — Bounded migration and monitoring

- Simulate one business-area migration.
- Human-review near duplicates and authority conflicts.
- Migrate one approved batch with before/after and recovery receipts.
- Enable Drive events for approved intake folders after replay tests.

**Exit:** coverage, exceptions, duplicates, access and recovery are evidenced.

## Target repository

```text
pmps-docs/
├── config/
├── schemas/
├── policies/
├── src/foundations/
│   ├── api/
│   ├── workflows/
│   ├── agents/
│   ├── ingestion/
│   ├── knowledge/
│   ├── interviews/
│   ├── drafting/
│   ├── audit/
│   └── adapters/
├── tests/{contract,policy,workflow,security,golden-corpus}/
├── deploy/
├── manifests/
└── docs/
```

The first milestone is a CLI/API command that accepts a declared corpus manifest and returns an ingestion receipt, parsed manifest, proposed claims, contradictions/gaps, targeted interview dossier and complete audit events.
