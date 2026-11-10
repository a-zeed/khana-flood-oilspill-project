# Week 10: GeoPandas, layers as tables

## What this folder contains

Guided scripts (Ibadan North teaching data):
- explore_pandas.py: first look at the ward population table
- filter_sort.py: filters, sorts and adds a column
- explore_layer.py: opens wards.gpkg and checks rows, geometry, CRS and bounds
- geom_props.py: looks inside one ward geometry
- csv_to_points.py: turns the health facility CSV into a point layer
- join_population.py: joins population to ward polygons after cleaning names
- make_map.py: map of health facilities over the wards
- save_outputs.py: writes the wards table and a GeoPackage copy
- facilities_map.png and wards_table.csv: outputs of the guided scripts

Challenge files (my own Khana data):
- my_explore.py: checks my settlements-near-waterways layer
- my_points.py: writes my 2 waterway points to a coordinates CSV, reads it back as points and checks they land inside the Khana outline (writes data/processed/waterway_points.csv and waterway_points.gpkg)
- my_points_check.png: the check map for my_points.py
- my_join.py: joins my 100-row settlements table to the 1815-row settlements layer on block_id
- my_map.py and my_map.png: one map of Khana LGA showing settlements, settlements near waterways, waterway lines and points

## How to run it

From the repository root, for example:
`uv run month-03/week-10/my_explore.py`

## What I found

My settlements-near-waterways layer has 100 polygons in EPSG:32632 (metres). Its bounds convert to about 4.57 to 4.76 degrees north and 7.31 to 7.52 degrees east, which is where I expect Khana LGA in Rivers State to be. Joining my 100-row table to the 1815-row settlements layer on block_id matched 100 of 100 on the first try, so no cleaning was needed. I checked that the block_id values are unique, that none are blank, and that the layer still has 1815 rows after the join. My 2 waterway points both land inside the Khana outline.

## What went wrong and how I fixed it

- **Folder names.** I first named my folders month3 and week_10, and at one point Month-3, so uv run could not find my scripts and said "Failed to spawn". Renaming them to month-03 and week-10, exactly as the task says, fixed it.
- **Wrong terminal folder.** I ran scripts from the parent folder GEODEV_Git_repo instead of the repository folder inside it, which gave the same error. I fixed it by opening the repository folder itself in VS Code, so the terminal starts in the right place.
- **uv add failed.** My first uv add for geopandas, rasterio and matplotlib stopped with "Expected a Python module at src\geodev\__init__.py". The src folder from Week 6 had never been uploaded to GitHub, so my clone did not have it. I copied src from my old GEODEV folder into the clone and the install worked.
- **Wrong data files on GitHub.** A scan of my old GEODEV folder and the clone showed that some data files in the clone were not my processed Month 1 versions: the study area files held all 774 LGAs instead of Khana only, and the waterway lines files held points instead of 49 lines. I do not know exactly how they got there. I replaced them with my originals, checked the row counts (1, 1, 49, 49, 2 and 2) and pushed the fix.
- **A 2 GB file in the clone.** When I copied files into the clone, a settlements file of about 2 GB came with them. git status showed it as untracked, so I deleted it from the clone before committing, because GitHub refuses files over 100 MB. The original is still in my old GEODEV folder.