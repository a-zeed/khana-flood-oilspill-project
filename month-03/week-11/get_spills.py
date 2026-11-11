import json
import gzip
import urllib.request
import pandas as pd

URL = "https://oilspillmonitor.ng/api/spill-data.php?dataset=nosdra&format=json"

request = urllib.request.Request(URL, headers={"User-Agent": "GeoDevLab-student-script"})
with urllib.request.urlopen(request, timeout=60) as response:
    raw = response.read()
if raw[:2] == b"\x1f\x8b":
    raw = gzip.decompress(raw)
spills = pd.DataFrame(json.loads(raw.decode("utf-8")))
print("All records:", len(spills))

spills["lat"] = pd.to_numeric(spills["latitude"], errors="coerce")
spills["lon"] = pd.to_numeric(spills["longitude"], errors="coerce")

by_name = spills["lga"].fillna("").str.strip().str.lower() == "khana"
in_box = spills["lat"].between(4.56, 4.83) & spills["lon"].between(7.30, 7.55)
usable = (spills["status"].fillna("") != "invalid") & (spills["contaminant"].fillna("") != "gs")

keep = spills[(by_name | in_box) & usable].copy()
keep["matched_by_lga_name"] = by_name[keep.index]
print("Kept:", len(keep), "| matched by LGA name:", int(keep["matched_by_lga_name"].sum()))

columns = ["id", "status", "company", "incidentnumber", "incidentdate", "contaminant",
           "estimatedquantity", "cause", "sitelocationname", "latitude", "longitude",
           "lga", "statesaffected", "matched_by_lga_name"]
keep.reindex(columns=columns).to_csv("data/raw/khana_spills_api.csv", index=False)
print(keep[keep["id"].isin(["471083", "404073", "6300"])][["id", "incidentdate", "latitude", "longitude"]])