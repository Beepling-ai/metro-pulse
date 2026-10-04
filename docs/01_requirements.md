# 01 · Discovery and requirements

## Kickoff workshop (week 0, day 2)
Attendees: OCC Head (sponsor), 2 station controllers, DMRL IT manager, AFC vendor engineer, QR vendor product
manager, DMRL information security. Lakehouse Labs: engagement manager, tech lead, 2 data engineers, BI developer.

### Questions we asked, and the answers we got

| # | Question | Answer | Impact |
|---|---|---|---|
| 1 | How fast must an alert reach the OCC? | "Within 10 minutes of crowding starting is a big improvement. Today it's 20+." | Micro-batch every 5–10 min is enough. No need for sub-second streaming. |
| 2 | What counts as dangerous? | "Our safety team has platform capacity numbers, but not in a system." | Open question OQ-04. We'll start with assumed values, the client must confirm. |
| 3 | How does AFC data reach us? | CSV every 5 min to an SFTP folder, with a control file holding the row count. | Bronze must reconcile against control totals. |
| 4 | Timezone of AFC timestamps? | AFC engineer: "Station local time." No timezone in the file. | Parse as IST explicitly. Write it in the data contract. |
| 5 | Are entry and exit both captured? | Yes, for smart cards and tokens. Exit carries the fare. | Trips are possible for AFC media. |
| 6 | What happens when a station loses its network? | Station server buffers and uploads later, sometimes 20+ minutes late. | Late data is guaranteed. Watermark decision needed (ADR-002). |
| 7 | Can the vendor re-send a file? | Yes, after a failed upload, with an `_R1` suffix. | Duplicates guaranteed. Dedupe on DEVICE_ID + TXN_SEQ. |
| 8 | How do QR validations reach us? | JSON events pushed every 30 s. At-least-once delivery. UTC epoch milliseconds. | Second timezone format. Dedupe on eventId. |
| 9 | Does QR send the fare? | No, fares live in the booking system. | Revenue from QR is out of scope (gap G-06). |
| 10 | Are card numbers personal data? | InfoSec: "Treat smart card IDs as personal identifiers." | Hash in silver. Restrict bronze. |
| 11 | Who fixes wrong station codes? | Planning team owns the master, but it's updated rarely. | We maintain a mapping file in Git with a change process. |
| 12 | Who supports the system after go-live? | DMRL IT, 2 engineers, business hours, plus on-call rota. | Runbook, alerts by email, simple deployment. |

## Requirements

### Functional
| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Show tap-ins and tap-outs per station per minute | Must |
| FR-02 | Show a crowding index and level (green, amber, red) per station, refreshed at least every 10 min | Must |
| FR-03 | Raise an alert when a station stays red, and clear it when crowding drops | Must |
| FR-04 | Show riders currently inside the network | Should |
| FR-05 | Origin to destination trips and journey times for planning | Could |
| FR-06 | Revenue per station from AFC fares | Could |

### Non-functional
| ID | Requirement | Target |
|---|---|---|
| NFR-01 | Freshness: event happens to dashboard | Under 10 min for 95% of events (excluding upstream outages) |
| NFR-02 | Correctness | No double counting of re-sent files or duplicate QR events |
| NFR-03 | Completeness | Every AFC file reconciled against its control total |
| NFR-04 | Privacy | No raw card or ticket numbers outside bronze |
| NFR-05 | Operability | Job failures alert by email. Every alert has a runbook entry. |
| NFR-06 | Deployability | One-command deploy to dev and prod, from Git |
| NFR-07 | Cost | Runs on serverless compute, no always-on clusters |

## Scope
| In scope (phase 1) | Out of scope |
|---|---|
| AFC and QR ingestion, station crowding, alerts, DQ monitoring, dashboard, CI/CD, runbook | Train positions and platform sensors (no data available) |
| Origin-destination trips (stretch) | QR revenue (fare not sent) |
| Handover and 1 week of hypercare | Passenger-level analytics or profiling (privacy) |

## Open questions (tracked in the RAID log)
| ID | Question | Owner | Due |
|---|---|---|---|
| OQ-01 | Official definition of a "red" station | OCC safety lead | Sprint 1 |
| OQ-02 | Which email or group receives alerts? | DMRL IT | Sprint 2 |
| OQ-03 | Retention for bronze raw data (legal) | DMRL InfoSec | Sprint 2 |
| OQ-04 | Platform capacity per station (safe entries per 5 min) | OCC safety lead | Sprint 1 |
| OQ-05 | Should depot test gate (TST) data be kept anywhere? | AFC vendor | Sprint 1 |
