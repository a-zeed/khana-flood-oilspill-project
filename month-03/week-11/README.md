# Week 11: CRS and spatial operations

## What this folder contains

Guided scripts (Ibadan North teaching data):
- area_wrong_and_right.py: why area in degrees is wrong, and the right area in metres
- set_vs_to.py: set_crs relabels, to_crs recalculates
- one_point.py: transforming one coordinate with pyproj
- spatial_ops.py: buffers and counting facilities per ward
- coverage_gap.py: the parts of each ward more than 2 km from a facility
- nearest.py: distance from each ward centre to the nearest facility
- clip_dissolve.py: clipping roads to a ward and dissolving wards into an LGA
- fix_geometry.py: finding and repairing an invalid shape

Challenge scripts (my own Khana data):
- my_crs.py: CRS check and reprojection to EPSG:32632, area and length
- get_spills.py: downloads NOSDRA oil spill records and keeps those in or near Khana
- prepare_flood.py: clips two UNOSAT flood layers to Khana
- my_count.py: counts spills and measures flood water in 5 km cells, and writes the combined table and the map
- my_reach.py: distance from each spill to the nearest waterway
- my_validity.py: checks my layers for invalid geometry
- my_count_map.png: map of flood water (2022 and 2024) with the spills

Result layers in data/processed/: khana_cells_spills_floods.csv and .gpkg (one row per 5 km cell), khana_flood_2022.gpkg and khana_flood_2024.gpkg.

## How to run it

From the repository root, for example:
`uv run month-03/week-11/my_crs.py`
prepare_flood.py reads the UNOSAT downloads from my Downloads folder, so it cannot be rerun without them; its results are saved in data/processed/.

## EPSG code and why

I used EPSG:32632 (WGS 84 / UTM zone 32N). Khana LGA lies at about 7.3 to 7.5 degrees east, which is inside zone 32N (6 to 12 degrees east), and estimate_utm_crs() suggested the same code. The Ibadan teaching data uses EPSG:32631 because Ibadan is further west.

## What I measured

- Khana study area: 523.4 km2. Waterway lines: 94.45 km.
- Spills: 6 records kept from the NOSDRA Oil Spill Monitor feed (retrieved on 11 November 2026); 3 fall inside the Khana outline. In a 5 km grid of 32 cells, 2 cells contain spills, and the count check printed 3 of 3.
- Flood water inside Khana from UNOSAT satellite maps (VIIRS, 375 m): 6.82 km2 (1.3%) in the 13 to 17 October 2022 window, with 25.9% of Khana under cloud; 17.95 km2 (3.4%) in the 9 to 13 November 2024 window, with 0.3% under cloud. 12 cells show some flood water in each year, and 2 cells have both a spill and flood water.
- Nearest waterway to each spill inside Khana: 85 m, 962 m and 2287 m.
- Invalid geometries: none in my five layers (study area, settlements, settlements near waterways, waterway buffer, waterway lines).

## Choices

For my_reach.py I used the nearest distance, because my question is how close recorded spills are to waterways. For my_count.py the Khana outline is a single polygon, so I counted in a 5 km grid to get real counts and zeros. I kept spill records that name Khana as the LGA or fall in a box around the study area, then checked them against the outline, and I left out records marked invalid and contaminant "gs" (I assume this means gas).

## Limitation

Only 3 recorded spills fall inside Khana, and they were recorded between 2008 and 2026, while the flood maps cover single 5-day windows in October 2022 and November 2024. So a cell that has both a spill and flood water means the same place, not the same time, and says nothing about cause. The spill records depend on what is reported and are incomplete. The flood layers are 375 m resolution, so narrow creeks and small flooded patches are missed, the 2022 map had a quarter of Khana under cloud, and UNOSAT lists the confidence of these layers as "To be evaluated".
