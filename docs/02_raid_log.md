# 05 · Project plan and backlog

## Team

| Role | Who | Responsibilities |
|---|---|---|
| Engagement manager | Lakehouse Labs | Client relationship, scope, budget, status reports |
| **Tech lead** | Lakehouse Labs | Architecture, ADRs, code reviews, technical risks, client technical decisions |
| Data engineer ×2 | Lakehouse Labs | Ingestion, silver, gold, alerts, tests |
| BI developer | Lakehouse Labs | Dashboard, SQL alerts, UAT support |
| QA (part time) | Lakehouse Labs | Test plan, UAT scripts |
| Product owner | DMRL OCC Head | Priorities, acceptance, sign-off |
| SMEs | AFC vendor, QR vendor, OCC safety lead | Data questions, thresholds |
| Support team | DMRL IT | Receives handover, runs prod |

## RACI (R = does it, A = accountable, C = consulted, I = informed)

| Activity | Tech lead | Data eng | BI | DMRL OCC | DMRL IT | Vendors |
|---|---|---|---|---|---|---|
| Architecture & ADRs | A/R | C | C | I | C | C |
| Source onboarding | A | R | | I | C | R |
| Pipelines & tests | A | R | | | I | |
| Thresholds & alert rules | C | R | C | A | I | |
| Dashboard | C | C | R | A | I | |
| Deployment & CI/CD | A | R | | | C | |
| UAT & sign-off | R | C | C | A | C | |
| Handover | A/R | R | R | I | C | |

## Timeline (7 weeks)

| Week | Phase | Goal | Exit criteria |
|---|---|---|---|
| 0 | Inception | Discovery, access, architecture | Requirements and ADRs signed off, data access granted |
| 1–2 | Sprint 1 | Foundations + ingestion | Both sources landing in bronze in dev, mapping file agreed |
| 3–4 | Sprint 2 | Silver, gold, alerts | Crowding index and alerts working on dev data |
| 5–6 | Sprint 3 | DQ, CI/CD, dashboard, UAT | UAT passed, prod deployed |
| 7 | Hypercare | Live support + handover | Runbook walkthrough done, support accepted by DMRL IT |

## Ceremonies
Daily standup (15 min) · Sprint planning and review every 2 weeks with the OCC · Weekly status report to the sponsor ·
Weekly RAID review (risks, assumptions, issues, dependencies).

## Backlog
Full Jira-importable list: `tasks/backlog.csv`. Summary:

| Epic | Key tickets | Sprint |
|---|---|---|
| E1 Project setup | MP-1 Git repo + branch rules · MP-2 Dev/prod schemas · MP-3 Asset Bundle skeleton · MP-4 CI with tests | S1 |
| E2 Source onboarding | MP-5 AFC SFTP access + sample files · MP-6 QR feed access · MP-7 Profile both sources · MP-8 Station code mapping | S1 |
| E3 Bronze | MP-9 AFC CSV ingestion · MP-10 AFC control files · MP-11 QR JSON ingestion | S1 |
| E4 Silver | MP-12 Standard event schema · MP-13 Station mapping join · MP-14 Validation + quarantine · MP-15 Dedupe · MP-16 Rider hashing | S2 |
| E5 Gold | MP-17 Station flow 1-min · MP-18 Crowding 5-min · MP-19 Trips (OD) · MP-20 Serving views | S2 |
| E6 Alerts | MP-21 Alert state machine + tests · MP-22 Alert job task · MP-23 SQL alert to OCC email | S2–S3 |
| E7 Observability | MP-24 DQ monitor (8 checks) · MP-25 Job failure emails · MP-26 Runbook | S3 |
| E8 Release | MP-27 Prod deploy pipeline with approval · MP-28 Simulator for dev only | S3 |
| E9 Dashboard & UAT | MP-29 OCC dashboard · MP-30 UAT with controllers | S3 |
| E10 Run | MP-31 Map "Lakdi-ka-pul" (found in prod) · MP-32 Handover session · MP-33 Hypercare | S3–W7 |

## Definition of Ready
A ticket has a clear goal, acceptance criteria, known data source, and no blocking dependency.

## Definition of Done
Code reviewed and merged · unit tests pass in CI · deployed to dev via the bundle · DQ checks pass ·
docs updated (contract, runbook, ADR if a decision changed) · demoed to the product owner.

## RAID log (top items)

| Type | Item | Owner | Mitigation |
|---|---|---|---|
| Risk | Capacity numbers not provided in time (OQ-04) | OCC | Assumed values, clearly labelled on the dashboard |
| Risk | AFC vendor changes file format without notice | AFC vendor | Data contract + bronze as strings + DQ-02 |
| Assumption | 10-min latency is acceptable | OCC | Signed off in requirements |
| Issue | Client master has wrong code for Raidurg | Planning team | Mapping uses AFC's `RDM`; correction requested |
| Dependency | SFTP and QR access from DMRL IT | DMRL IT | Escalate in week 0 if not ready by day 3 |
