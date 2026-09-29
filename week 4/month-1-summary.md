# Month 1 summary

## Question
Which settlements in Khana LGA, Rivers State, sit on low-lying land near watercourses — areas more exposed to oil spill spread and flooding?

## Operation
Buffered the OpenStreetMap waterway lines (76 features) by 200 m, dissolved into one corridor shape, then used Select by Location to find which settlement blocks (from GRID3's settlement extents, clipped to Khana) intersect that buffer. This operation was chosen because it answers the "near watercourses" half of the project question directly — it does not yet cover the "low-lying" half, which needs elevation data (not yet acquired).

## Expected
Before running the analysis, I expected roughly 25–40% of the 1,815 settlement blocks (about 450–725) to fall within 200 m of a waterway, based on the earlier map showing waterways running through the densest settlement clusters.

## Got
Only 100 of 1,815 settlement blocks (about 5.5%) intersect the 200 m buffer — far fewer than expected.

## What surprised me
The gap between the expectation (25–40%) and the actual result (5.5%) was large. A few likely reasons: only 76 waterway lines are mapped in OSM for this LGA, and many settlement clusters sit further from the mapped rivers/streams than the map's visual impression suggested. A 200 m buffer is also a fairly narrow corridor. This is a useful reminder that "waterways run through the settlement clusters" (true at LGA scale) doesn't mean most individual settlement blocks are close to water — it may be a smaller number of large, dense clusters sitting directly on the water that drove that visual impression.

## Checks performed
- **Map check:** the 100 selected settlement blocks visually sit along the buffer corridor; unselected blocks sit clearly outside it.
- **Count check:** 100 selected vs. an expectation of 450–725 — confirmed as a large, real gap, not just noise.
- **Hand verification:** manually measured one selected block and one unselected block against the nearest waterway line; the selected block fell within 200 m, the unselected block did not.
- **Empty geometry check:** ran `is_empty_or_null($geometry)` on the settlement layer — 0 features selected, confirming no empty or missing geometries.

## What I still need
- **Elevation data** (SRTM or Copernicus DEM via OpenTopography) to identify which of these 100 near-waterway settlements also sit on genuinely low-lying land — this is the second half of the project question and hasn't been addressed yet.
- Ideally, a settlement-name dataset, since the current settlement layer is building-block level (no names), which limits how findings can be communicated (by location/coordinates rather than named villages).
