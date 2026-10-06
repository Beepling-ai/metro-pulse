# Data profile

## Source 1: Client station master (reference/client_station_master.csv)
Received: from the client's planning team (Excel export)

| # | Check | Result | Impact | Action |
|---|---|---|---|---|
| 1 | Row count | 57, matches our STATIONS | - | - |
| 2 | Order | Same as our HM01-HM57 | Can match by position | - |
| 3 | Name format | ALL CAPITALS | Name joins fail unless case is normalised | Join on IDs, not names |
| 4 | Interchanges | 3 marked Y, correct | - | - |
| 5 | OPENED column | Empty for all 57 | Can't place stations in time | Ask client (RAID log) |
| 6 | AFC_CODE | (fill in after task 4.4) | | |
