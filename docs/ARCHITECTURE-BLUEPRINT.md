# PMPS Business Foundations Engine — Locked Architecture

**Status:** LOCKED FOR PILOT BUILD
**Date:** 2026-08-02
**Approvers:** Ashley Halvorson (PMPS operations); Eli Halvorson (architecture, security and production)

## Outcome

Build a reusable, tenant-configured engine that ingests a business corpus, creates a source-grounded operating model, detects gaps, runs targeted post-ingestion interviews, drafts improvements and emits controlled foundations for future agents. PMPS is the proving tenant; PMPS-specific folders, people, systems and jurisdiction are configuration.

## Authority boundaries

- Google Drive: business originals and issued controlled files.
- Master Document Register: document identity and lifecycle.
- GitHub: schemas, policies, prompts, evaluations and deployment configuration.
- PostgreSQL: workflow state, business ontology, knowledge claims and append-only operational events.
- Existing EmpireMind memory/audit systems: approved projections, not replaced.
- Notion and Linear: rebuildable human projections.
- Xero, JobAdder, TrackEasy and nominated applications: transactional authority.

Agents propose. OPA policy controls allowed routes and gates. Humans approve consequential actions. Containers receive no Docker socket, credential store, browser profile or unrestricted host mount.

## Closed learning loop

```text
REGISTER SOURCES -> INVENTORY READ-ONLY -> QUARANTINE + SCAN
-> SHA-256 + PARSE + PII CLASSIFICATION
-> PROVISIONAL BUSINESS MODEL -> CONTRADICTIONS + GAPS
-> TARGETED INTERVIEWS -> CONFIRMED CLAIMS
-> IMPROVEMENT PROGRAMME -> CONTROLLED DRAFTS + AGENT SPECS
-> INDEPENDENT AUDIT + HUMAN/LEGAL GATES
-> ISSUE + DRIVE READBACK -> DRIFT + DELTA LEARNING
```

The engine learns by promoting reviewed atomic claims, not by memorising every extracted sentence.

## Component ownership

### Durable control plane

- **Temporal:** workflows, retries, timers, approval pauses, compensation and replay.
- **OPA:** routing, sensitivity, retention, approval, jurisdiction and tool policy.
- **PostgreSQL + pgvector:** operational state, ontology, claims, gaps and retrieval metadata.
- **Hash-chained ledger:** append-only operational events; sanitized attestations project to existing EmpireMind audit/evidence surfaces.

### Bounded agent plane

Google ADK workers are dispatched by Temporal: Corpus Analyst, Business Modeller, Gap Assessor, Interview Planner, Interviewer, Document Architect, Drafting Specialist and Independent Auditor.

Agents cannot call each other arbitrarily. Every output validates against JSON Schema before progressing.

### Ingestion plane

- Google Workspace Events API + Pub/Sub for commissioned Drive events.
- Read-only bounded inventory for the initial pilot.
- ClamAV before extraction.
- Docling as the default local parser.
- Google Document AI as a policy-gated fallback for difficult scans/forms/tables.
- NVIDIA NeMo Retriever as an optional benchmark, not a v1 dependency.
- Presidio for local PII detection/redaction.
- Originals stay in Drive; restricted parsed derivatives have encryption, access control and expiry.

### Safe tools and inference

- Google MCP Toolbox exposes named, parameterized PostgreSQL/BigQuery tools; production agents receive no generic SQL tool.
- Drive, Notion, Linear and EmpireMind adapters require idempotency, readback and correction paths.
- Ollama handles private low-risk first passes.
- Approved cloud models receive minimum policy-permitted context.
- NeMo Guardrails may add conversational rails; OPA remains the authorization boundary.
- Host work occurs only through a signed allowlisted bridge.

### Evaluation and observability

- OpenTelemetry is the trace/metric standard.
- Existing Prometheus/Grafana is reused only after live commissioning.
- Google ADK eval sets measure specialist quality.
- NVIDIA garak is a release gate for prompt injection and LLM vulnerabilities.
- Every report states explicit corpus, parse, claim-review, control and exception numerators/denominators.

## Canonical records

`tenant`, `source_system`, `source_record`, `document_record`, `content_artifact`, `business_entity`, `process_record`, `process_step`, `role_record`, `system_authority`, `knowledge_claim`, `claim_evidence`, `contradiction`, `obligation`, `risk`, `control`, `gap_finding`, `interview_session`, `draft_package`, `agent_specification`, `approval_request`, `approval_receipt`, `migration_item`, `audit_event`.

Every material claim contains a source record and locator, extraction method, confidence, freshness, sensitivity and review state. Review states are `PROPOSED`, `CONFIRMED`, `CORRECTED`, `CONTRADICTED`, `STALE`, `REJECTED` and `SUPERSEDED`.

## Post-ingestion interviews

1. Generate a dossier showing the inferred process, sources, contradictions, missing owners and high-risk unknowns.
2. Rank questions by expected information gain multiplied by business/legal risk.
3. Run a 15–30 minute adaptive voice/chat interview.
4. Ask for a recent real example for claims affecting money, people, safety, contracts or external communication.
5. Classify answers as `CONFIRM`, `EXTEND`, `CORRECT`, `CONTRADICT` or `UNKNOWN`.
6. Require human approval of the claim summary before promotion.
7. Keep raw audio/transcripts restricted; promote approved atomic claims only.

## Agent-ready outputs

For every confirmed process the engine emits purpose, triggers, inputs/outputs, completion definition, RACI, authority, systems of record, business rules, exceptions, evidence, retention, approvals, prohibited actions, typed tools, events, idempotency, SLOs, test cases and residual human judgment.

## Deployment

### Pilot

- Windows workspace for code, tests and operator control.
- Pinned Docker Compose: Temporal, PostgreSQL, OPA, MCP Toolbox, API/worker, parser and OpenTelemetry.
- Declared pilot corpus is mounted read-only.
- Drive writes remain disabled until routing, approval and readback tests pass.

### Commissioned runtime

- Mac Studio: private inference, parsing acceleration and retrieval adapters after live security/restore commissioning.
- Google Cloud `australia-southeast1`: Pub/Sub, Cloud Run adapters, approved encrypted derivatives, audit projection and backups.
- MacBook Pro: operator workstation only; no production control-plane dependency and no new independent LaunchAgents.

## EmpireMind convergence

| Existing asset | Use |
|---|---|
| `librarian` | Source registry, inventory and delta/coverage feed |
| `nlm-brain` | Question-bank, blind-spot and convergence patterns |
| `pmps-ai-memory` | Entity vocabulary and approved-claim projection |
| `pmps-core` | Historical evidence only |
| `pmps-evidence` | Sanitized signed proof and commissioning receipts |
| `pmps-pty-ltd-ops` | Document AI, BigQuery, MERGE and consumer-contract patterns |
| `agentos-control-plane` | Read-only health projection |
| `pmps-migration` / `pmps-runbooks` | Migration, operations and recovery |

No existing repository is silently modified.

## Commissioning definition

- idempotent identical input and versioned changed bytes;
- exact/near-duplicate handling proven;
- restricted data cannot leak to broad indexes/projections;
- every confirmed claim resolves to evidence;
- interview correction preserves source history;
- approvals bind exact identity, version and SHA-256;
- Drive write is read back;
- recovery does not repeat external writes;
- audit replay reconstructs lifecycle;
- backup restore demonstrated;
- garak and injection suites pass;
- one SOP produces a complete, tested agent specification.

## Official upstreams

- https://github.com/google/adk-python
- https://github.com/GoogleCloudPlatform/agent-starter-pack
- https://github.com/googleapis/mcp-toolbox
- https://github.com/GoogleCloudPlatform/document-ai-samples
- https://developers.google.com/workspace/drive/api/guides/events-overview
- https://github.com/NVIDIA/NeMo-Retriever
- https://github.com/NVIDIA-NeMo/Guardrails
- https://github.com/NVIDIA/garak
- https://github.com/NVIDIA-NeMo/Curator
- https://github.com/NVIDIA-NeMo/Anonymizer
- https://github.com/NVIDIA/skills
