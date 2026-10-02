# 00 · The client request (how this project starts)

> Fictional engagement for portfolio purposes. "Deccan Metro Rail Ltd" (DMRL) is an invented client operating
> a metro network modelled on Hyderabad's three lines. Our company is "Lakehouse Labs", a data consultancy.

---

**From:** Head of Operations Control Centre (OCC), DMRL
**To:** Engagement Manager, Lakehouse Labs
**Subject:** RFP – Live station crowding visibility

Hi team,

Last month we had two serious crowding incidents at Miyapur and LB Nagar during the morning peak. In both cases
our controllers only found out from CCTV and phone calls, about 20 minutes after it started. After the IPL match
at Uppal stadium we had a similar issue at Stadium station.

We want a system that tells the OCC **which stations are getting dangerously crowded, as it happens**, so we can
send staff, open extra gates, and request extra trains.

What we have:
- Our fare-gate (AFC) vendor already exports transactions every few minutes. Our IT team can give you access.
- About 30% of riders now use QR tickets from the mobile app, which is run by a different vendor.
- A station master spreadsheet maintained by our planning team.

What we need:
1. A live view of crowding at all 57 stations.
2. Alerts when a station becomes unsafe.
3. Origin to destination travel patterns for the planning team (not urgent).
4. Something our IT team can run and support after you leave.

Budget is approved for about 7 weeks. Please send your approach and plan.

Regards,
Head of OCC, DMRL

---

## What the tech lead notices immediately (before the kickoff)

| Statement in the email | Hidden question we must answer in discovery |
|---|---|
| "as it happens" | How fast exactly? Seconds, or minutes? This decides architecture and cost. |
| "dangerously crowded" | Who defines the threshold? We need a number per station, from the client. |
| "exports every few minutes" | Format? Delivery method? Timezone? Does it include both entry and exit? |
| "QR tickets … different vendor" | Second source with a different format. Who owns that contract? |
| "station master spreadsheet" | Manually maintained, so expect mismatches with the systems. |
| "IT team can run and support" | We need CI/CD, a runbook, monitoring, and a handover plan from day one. |
| "about 7 weeks" | Fixed timeline, so phase 1 must be scoped tightly. Origin-destination is a stretch goal. |
