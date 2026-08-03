# ADR-001: Open-Source Stack

**Status:** ACCEPTED FOR PILOT
**Date:** 2026-08-02
**Deciders:** Ashley Halvorson (operations); Eli Halvorson (architecture/security)

## Decision

Use one component per concern and wrap every upstream behind an internal interface.

| Concern | Selected | Adoption |
|---|---|---|
| Durable workflow | Temporal | Core |
| Agent framework | Google ADK | Core |
| Production conventions | Google Agent Starter Pack | Core template source |
| Authorization | Open Policy Agent | Core |
| Database tools | Google MCP Toolbox | Core |
| Control store | PostgreSQL + pgvector | Core |
| Local parsing | Docling | Core |
| Difficult forms/scans | Google Document AI | Policy-gated fallback |
| PII detection | Microsoft Presidio | Core local layer |
| Malware scanning | ClamAV | Core intake layer |
| Local inference | Ollama | Core adapter |
| Telemetry | OpenTelemetry | Core |
| Adversarial evaluation | NVIDIA garak | Core release gate |
| Conversational rails | NVIDIA NeMo Guardrails | Benchmark; adopt if safety improves |
| Multimodal/high-volume parsing | NVIDIA NeMo Retriever | Optional benchmark |
| Large-scale curation | NVIDIA NeMo Curator | Deferred pending scale/GPU evidence |
| Context-aware anonymization | NVIDIA NeMo Anonymizer | Evaluate against Presidio |

## Explicit exclusions

- No ADK + LangGraph + DeepAgents stack. ADK owns bounded reasoning; Temporal owns workflow.
- No NVIDIA RAG Blueprint as the base runtime. Its supported production route assumes NVIDIA NIM/Kubernetes; the PMPS estate has no commissioned NVIDIA cluster.
- No Paperless, Mayan, OpenKM or second DMS beside Google Drive.
- No Neo4j core dependency. PostgreSQL is authoritative; Neo4j may become a rebuildable projection when graph-specific queries justify it.
- No A2A in v1. Adopt it only for independently deployed or third-party agents.
- No Google AX or NeMo Gym runtime dependency while their APIs remain rapidly evolving.
- No general SQL, host shell, Docker socket or credential-store tool exposed to an agent.

## Adoption rubric

Every dependency must score at least 80/100 and cannot score zero in security, licence or exit path.

| Dimension | Weight |
|---|---:|
| Solves a demonstrated gap | 20 |
| Security and privacy fit | 20 |
| Maintenance and release health | 15 |
| Container/offline support | 10 |
| Standards and interoperability | 10 |
| Licence/commercial usability | 10 |
| Observability and testability | 10 |
| Replacement/exit path | 5 |

Each upstream is pinned by release and image digest, added to the SBOM, vulnerability-scanned, wrapped behind a contract and tested against the PMPS golden corpus before promotion.

## Consequences

- Google and NVIDIA capability is reused without binding business rules to a model vendor.
- The pilot runs on CPU/Apple Silicon; NVIDIA acceleration remains an adapter option.
- Temporal adds operational complexity, accepted because human-paused replayable workflows are essential.
- EmpireMind Librarian, PMPS memory, evidence and monitoring remain in place behind explicit adapters.
