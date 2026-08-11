# PMPS Filing Standard — August 5 Generation

**Status:** Canonical configuration, non-private routes ready for controlled operation  
**Effective configuration date:** 2026-08-11  
**Filing generation:** 2026-08-05

## Canonical tree

```text
Premium Mobile Plant Solutions/
├── 00 Inbox
│   └── _Needs Review
├── 01 Growth
│   ├── Marketing & Brand
│   ├── Business Development
│   ├── Quotes & Tenders
│   └── Templates
├── 02 Workforce
│   ├── Worker Files
│   ├── Recruitment
│   ├── People Admin
│   └── Templates
├── 03 Operations
│   ├── Clients & Sites
│   ├── Rosters & Timesheets
│   ├── Safety
│   └── Assets
├── 04 Finance
│   ├── Invoices Out
│   ├── Bills In
│   ├── Receipts & Expenses
│   ├── Payroll
│   ├── Rates & Margin
│   └── Bank, Tax & BAS
├── 05 Enablement
│   ├── Insurance
│   ├── Suppliers & Purchasing
│   ├── Coal LSL
│   ├── IT & Systems
│   └── Company & Legal
├── 09 Governance
│   ├── Controlled Documents
│   ├── Master Register
│   ├── Policies
│   ├── SOPs & Playbooks
│   └── Brand Assets
├── 90 Private Vault
│   ├── Worker Medical & D&A
│   └── Pay & Personal
├── 99 Archive
└── _DUPLICATES_TO_REVIEW
```

## Operating rules

1. `00 Inbox` is the only intake lane. Agents never choose a final destination before hashing, metadata validation and deterministic policy.
2. Low-confidence, conflicting or incomplete items stay in Inbox and are recorded as exceptions.
3. Supplier invoices route to `04 Finance/Bills In`; sales invoices to `Invoices Out`; receipts to `Receipts & Expenses`.
4. Client and site evidence routes to `03 Operations/Clients & Sites`.
5. Controlled documents route to `09 Governance/Controlled Documents` only after human approval bound to exact version and SHA-256.
6. `90 Private Vault` is fail-closed until Google limited-access permissions are configured and tested. Payroll, medical and private HR records must remain in Inbox or their authoritative system until then.
   Proposed access principals are `ash@empiremind.ai` and `eli@empiremind.ai`; this declaration is not permission readback evidence.
7. `99 Archive` is lifecycle-only. No model may archive or dispose autonomously.
8. `_DUPLICATES_TO_REVIEW` is exception-only. Hash-identical duplicates may be proposed; non-identical candidates require human comparison.
9. July and August 1 filing scaffolds are legacy read-only. They are never routing targets and are not deleted during cutover.
10. Transactional truth remains in Xero, JobAdder, TrackEasy and nominated systems; Drive stores governed evidence, controlled files and pointers.

## Readiness state

- Folder existence and stable IDs: verified.
- Runtime configuration and deterministic routing: verified.
- Unit and golden-path tests: 10/10 passed.
- Container build: verified.
- Non-private route smoke test: verified.
- Master Document Register stable ID and canonical parent: verified.
- Master Document Register legacy location links: reconciliation pending.
- Private Vault limited access: blocked.
- Production Drive writer identity and write/readback canary: not commissioned.
- Legacy migration: not started.
