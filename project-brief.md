# My project brief

## The question

Which settlements in Khana Local Government Area, Rivers State, sit on low-lying land near watercourses — areas more exposed to oil spill spread and flooding?

## Why it matters

Khana LGA sits at the heart of Ogoniland, an area with a long, well-documented history of oil spill contamination and cleanup efforts (including UNEP's 2011 environmental assessment and the ongoing HYPREP cleanup programme). Low-lying settlements near rivers and streams are the most exposed when spills or floodwater spread, because oil and water both travel downhill toward drainage lines.

Environmental agencies such as NOSDRA, cleanup coordinators like HYPREP, and local community leaders could use the results to:
- Identify which settlements sit in the highest-risk terrain before a spill or flood event, rather than after
- Prioritise environmental monitoring and rapid-response resources toward the most exposed communities
- Support evidence-based conversations with oil companies and regulators about where contamination is most likely to spread and persist
- Give community organisations a clear, visual basis for raising concerns about specific settlements, rather than general appeals

Without this kind of screening, response efforts tend to be reactive — sent wherever a spill is reported rather than to where the underlying terrain makes communities most vulnerable in the first place.

## The data I need

- Local Government Area boundary (Khana) — GRID3
- Settlement extents — GRID3
- Elevation (to identify low-lying land) — OpenTopography (Copernicus DEM or SRTM, 30m)
- Watercourses (rivers and streams) — OpenStreetMap, via QuickOSM

## Where each dataset comes from

- LGA boundaries — GRID3 NGA – Operational LGA Boundaries — https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about — released March 2021 — GeoPackage
- Settlement extents — GRID3 NGA – Settlement Extents v4.1 — https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about — August 2026 — GeoPackage
- Elevation — OpenTopography (Copernicus DEM GLO-30, 30m) — https://portal.opentopography.org — GeoTIFF
- Watercourses — OpenStreetMap, extracted via QuickOSM (key: `waterway`) for Khana LGA extent — confirmed present, extracted 5 September 2026

## What I would build

A map that flags settlements in Khana LGA sitting on low-lying land within a set distance of a watercourse — a simple visual risk-screening tool. Over the course of the programme, this could grow into a dashboard that overlays real spill incident locations against this exposure map, giving cleanup teams a quick way to see which affected communities are also in flood-prone, low-lying terrain.
