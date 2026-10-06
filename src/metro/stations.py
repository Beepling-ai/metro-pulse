"""Hyderabad Metro network: 3 lines, 57 stations (3 interchanges).

Station order is approximate and for simulation only. Verify against HMRL before any real use.
"""

RED = ["Miyapur", "JNTU College", "KPHB Colony", "Kukatpally", "Dr. B.R. Ambedkar Balanagar", "Moosapet",
       "Bharat Nagar", "Erragadda", "ESI Hospital", "S.R. Nagar", "Ameerpet", "Punjagutta", "Irrum Manzil",
       "Khairatabad", "Lakdikapul", "Assembly", "Nampally", "Gandhi Bhavan", "Osmania Medical College",
       "MG Bus Station", "Malakpet", "New Market", "Musarambagh", "Dilsukhnagar", "Chaitanyapuri",
       "Victoria Memorial", "LB Nagar"]
BLUE = ["Nagole", "Uppal", "Stadium", "NGRI", "Habsiguda", "Tarnaka", "Mettuguda", "Secunderabad East",
        "Parade Ground", "Paradise", "Rasoolpura", "Prakash Nagar", "Begumpet", "Ameerpet", "Madhura Nagar",
        "Yusufguda", "Road No. 5 Jubilee Hills", "Jubilee Hills Check Post", "Peddamma Gudi", "Madhapur",
        "Durgam Cheruvu", "HITEC City", "Raidurg"]
GREEN = ["JBS Parade Ground", "Parade Ground", "Secunderabad West", "Gandhi Hospital", "Musheerabad",
         "RTC X Roads", "Chikkadpally", "Narayanguda", "Sultan Bazaar", "MG Bus Station"]
LINES = {"Red": RED, "Blue": BLUE, "Green": GREEN}

TERMINAL = {"Miyapur", "LB Nagar", "Nagole"}
RESIDENTIAL = {"JNTU College", "KPHB Colony", "Kukatpally", "Moosapet", "Bharat Nagar", "Erragadda", "Malakpet",
               "New Market", "Musarambagh", "Dilsukhnagar", "Chaitanyapuri", "Victoria Memorial", "Uppal", "NGRI",
               "Habsiguda", "Tarnaka", "Mettuguda", "Rasoolpura", "Prakash Nagar", "Madhura Nagar", "Yusufguda",
               "Musheerabad", "Chikkadpally", "Narayanguda", "Secunderabad West"}
OFFICE = {"HITEC City", "Raidurg", "Madhapur", "Durgam Cheruvu", "Jubilee Hills Check Post",
          "Road No. 5 Jubilee Hills", "Peddamma Gudi", "Begumpet", "Punjagutta", "Khairatabad", "Lakdikapul",
          "Assembly", "Dr. B.R. Ambedkar Balanagar"}
HUB = {"Ameerpet", "MG Bus Station", "Parade Ground", "Secunderabad East", "JBS Parade Ground", "Nampally",
       "Paradise", "RTC X Roads"}

# kind -> (demand weight, safe platform entries per 5 min, gates). Assumed values, to be confirmed by client (OQ-04).
KIND_DEFAULTS = {"terminal": (3.0, 420, 6), "residential": (1.2, 240, 6), "office": (1.5, 420, 8),
                 "hub": (2.5, 280, 12), "mixed": (0.8, 120, 6)}
BIG = {"Ameerpet": 4.0, "HITEC City": 3.0, "Raidurg": 2.5, "MG Bus Station": 3.0, "Secunderabad East": 2.5}


def _kind(name: str) -> str:
    for kind, group in (("terminal", TERMINAL), ("hub", HUB), ("office", OFFICE), ("residential", RESIDENTIAL)):
        if name in group:
            return kind
    return "mixed"


STATIONS: list = []
_index: dict = {}
for _line, _names in LINES.items():
    for _n in _names:
        if _n in _index:
            STATIONS[_index[_n]]["lines"].append(_line)
            continue
        _k = _kind(_n)
        _w, _cap, _g = KIND_DEFAULTS[_k]
        _index[_n] = len(STATIONS)
        STATIONS.append({"station_id": f"HM{len(STATIONS) + 1:02d}", "name": _n, "lines": [_line], "kind": _k,
                         "weight": BIG.get(_n, _w), "capacity_5min": _cap, "gates": _g})

BY_ID = {s["station_id"]: s for s in STATIONS}
BY_NAME = {s["name"]: s["station_id"] for s in STATIONS}
