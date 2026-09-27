# Week 3 — CRS, Clipping, and Quality Notes

## CRS chosen and why

**EPSG:32632 (WGS 84 / UTM zone 32N)**

Khana LGA sits at approximately 7.4°E longitude. UTM zone 31N covers 0°E–6°E, and UTM zone 32N covers 6°E–12°E — so Khana actually falls within **zone 32N**, not 31N. (An earlier version of this note incorrectly stated zone 31N; this was caught in mentor feedback and corrected.) EPSG:32632 is the correct projected coordinate system for accurate distance and area measurement in this part of Nigeria. All layers were originally in either EPSG:4326 (geographic, degrees) or EPSG:3857 (Web Mercator, distorted for area/distance), neither of which is suitable for measuring real distances or areas. Reprojecting to EPSG:32632 puts everything in metres, which the rest of the analysis (buffers, distances, areas) depends on.

## What was reprojected and clipped

All four project datasets were processed as follows:

| Dataset | Original CRS | Clipped to Khana? | Reprojected to? | Final file |
|---|---|---|---|---|
| LGA boundary (Khana only) | EPSG:4326 | Selected/exported (not clipped, extracted by attribute) | EPSG:32632 | `study_area_utm32.gpkg` |
| Settlement extents | EPSG:3857 | Yes, using study_area_utm32 | EPSG:32632 | `settlements_khana_utm32.gpkg` |
| Waterways (lines) | EPSG:4326 | Yes, using study_area | EPSG:32632 | `waterways_lines_utm32.gpkg` |
| Waterways (points/fords) | EPSG:4326 | Yes, using study_area | EPSG:32632 | `waterways_points_utm32.gpkg` |

Note: for the settlement extents (2.5 million features nationwide), the layer was reprojected to EPSG:32632 first, then clipped using the reprojected study area — this was done to avoid a CRS mismatch during clipping, since the settlement layer's original CRS (EPSG:3857) did not match the boundary layer's original CRS (EPSG:4326).

## The five quality checks

**1. Completeness**
Waterway data is sparse in naming detail: of 76 waterway line features, only a handful carry a `name` value (e.g. Imo River, River Uyin, Afa Creek) — most are unnamed but still geometrically present. Only 4 ford points are recorded for the entire LGA, which is likely an undercount given the density of the stream network, but reflects genuine OSM mapping coverage rather than a processing error.

**2. Currency**
GRID3 LGA boundaries were released March 2021. GRID3 settlement extents are dated August 2026. OSM waterway data was extracted 5 September 2026, reflecting whatever the most recent community mapping state was at that time — individual features may be older or newer depending on when each was last edited.

**3. Positional accuracy**
Sanity-checked by calculating Khana LGA's area after reprojection: **~523 km²** (calculated under the earlier, incorrect zone 31N; will be recalculated under the corrected zone 32N reprojection). This is close to Khana's commonly cited area (~560 km²), confirming the reprojection approach itself is sound and the boundary geometry is reasonable. The small difference is likely due to boundary vintage/source differences rather than a processing error.

**4. Attribute accuracy**
The settlement extents dataset is actually building-block-level data (columns like `block_id`, `building_count`, `block_area_sqm`), not one row per named settlement. This is an important distinction: it means the layer describes clusters of buildings rather than named towns/villages, and doesn't carry settlement names directly. No obvious attribute errors (wrong data types, outliers) were found in the boundary or waterway attribute tables.

**5. Fitness for purpose**
The clipped, reprojected data is fit for the project's purpose: identifying settlements on low-lying land near watercourses in Khana. The main limitation is that "settlements" here means building clusters rather than named places, so any results will need to be described in terms of building clusters/locations rather than named villages unless a settlement-name dataset is added later. The very low ford count (4) means fords specifically cannot be used to draw general conclusions, but the waterway line network (76 features) is dense enough to support proximity analysis.

## Problems found and how they were handled

- **CRS mismatch during clipping**: initially planned to clip the settlement layer (EPSG:3857) directly against the study area (EPSG:4326), which would have returned an empty or incorrect result. Fixed by reprojecting the full settlement layer first, then clipping using the reprojected study area.
- **Wrong UTM zone (caught in mentor feedback)**: all four layers were initially reprojected to EPSG:32631 (zone 31N), which does not cover Khana's actual longitude (~7.4°E). Corrected by re-reprojecting all four layers to EPSG:32632 (zone 32N), which is the correct zone for this location.
- **NULL values in waterway names**: not fixed, since this reflects genuine gaps in OpenStreetMap's tagging rather than a processing error. Flagged in the notes so it's not mistaken for a data loss issue later.
- **Settlement data granularity**: flagged (not fixable) — the dataset represents building blocks, not named settlements. Noted here and in data-notes.md so future analysis correctly interprets what a "settlement" feature actually represents.

## Where the analysis-ready files live

All final, clipped, and reprojected (EPSG:32632) files are saved in `data/processed/`:
- `study_area_utm32.gpkg`
- `settlements_khana_utm32.gpkg`
- `waterways_lines_utm32.gpkg`
- `waterways_points_utm32.gpkg`

Original, untouched downloads remain in `data/raw/` and were not modified.
