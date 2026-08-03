# Obsidian — Canon Ingest Rules

**ID:** `PMPS-STD-GOV-OBS-001`  
**Vault:** EmpireMind.ai (shared brain)  
**Role:** Searchable **mirror** of Foundations canon + working notes  
**Not:** Place where documents become official  

---

## 1. Folder (create exactly)

```text
03-Projects/pty-ltd/pmps-foundations/
├── 00-CANON-POINTER.md          ← always current; links out
├── HUMAN-SOP-mirror.md          ← summary + link to issued Drive/Git
├── ROADMAP-mirror.md
├── register-export/             ← optional CSV snapshots (no PII bodies)
├── decisions/                   ← D-PMP-*.md sanitized
└── working/                     ← scratch; never “ACTIVE”
```

Domain expert pack stays at:

`Domain Experts/Business Document Control/`  
→ Add banner at top of README_START_HERE: **Operational SoT moved to pmps-docs docs/canon + Drive Register (2026-08-03). This pack is REFERENCE standards library.**

---

## 2. Ingest protocol (when canon changes)

1. Pull/push `EmpireMind.ai` vault as usual.  
2. Update `00-CANON-POINTER.md` with:
   - Git commit SHA of `pmps-docs` canon  
   - Drive workspace link  
   - Notion Approved DB link  
   - Linear project link  
3. Optionally paste **short** roadmap phase table (no secrets).  
4. Do **not** bulk-import controlled PDF bodies into Obsidian.  
5. For each ACTIVE doc you care about offline: one note with YAML:

```yaml
---
doc_id: PMPS-PRO-OPS-012
status: ACTIVE_CANONICAL
version: "1.0"
sha256: "..."
drive: https://drive.google.com/...
notion: https://notion.so/...
bu: pty-ltd
canon: true
---
```

6. Graph links: `[[00-CANON-POINTER]]` from all Foundations notes.

---

## 3. Anti-drift

| If Obsidian says… | Truth is… |
|-------------------|-----------|
| Different version than Register | Register |
| Doc “approved” with no sha256 | Not approved |
| New Foundations process invented in daily note | Draft until CANON PR |

**Agents:** On session start for Foundations work, read `00-CANON-POINTER.md` then Git CANON.md.

**Revision:** 2026-08-03.r1
