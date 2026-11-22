# Week 12: Rasters with Rasterio

## What this folder contains

Guided scripts (Ibadan North teaching rasters):
- inspect_raster.py, read_values.py, pixel_coords.py, sample_points.py: inspecting a raster, reading it with nodata masked, converting between pixels and coordinates, and sampling elevation at points
- ndvi.py: NDVI from the Landsat red and near-infrared bands, with the scale factor applied
- plot_raster.py: writes ndvi_map.png
- clip_raster.py, zonal_stats.py, reproject_raster.py: clipping a DEM, mean elevation per ward, and reprojecting a raster

Challenge scripts (my own Khana data):
- my_inspect.py: inspection checks on my DEM, NDVI and NDWI rasters
- my_index.py: NDVI and NDWI from my Landsat scene, cut to the Khana outline with a cloud mask
- my_zonal.py: mean elevation, NDVI and NDWI per 5 km grid cell, saved as khana_cell_zonal_stats.csv
- my_map.py: writes my_map.png

## Data used

- DEM: SRTM 1 Arc-Second Global, tile N04E007 (version 3). The elevation data was collected in February 2000 by the Shuttle Radar Topography Mission, and this version was published on 23 September 2014; I downloaded it from USGS EarthExplorer on 21 November 2026. 3601 x 3601 cells, EPSG:4326, int16, nodata -32767.
- Landsat scene: LC09_L2SP_188057_20241219_20241220_02_T1 (Landsat 9, Tier 1, path 188 row 057), acquired 19 December 2024. Land cloud cover 10.89 percent (scene cloud cover 19.23 percent); after masking, 0.2 percent of Khana was under cloud, cloud shadow or dilated cloud. Bands 3, 4 and 5 and the quality band, from USGS EarthExplorer (Collection 2 Level-2).
- The rasters stay on my laptop and are described in data-notes.md.

## What I found

- My DEM, NDVI and NDWI rasters all pass the check that width times resolution equals right minus left, and the same for height.
- NDVI over Khana ranges from 0.013 to 0.858 with a mean of 0.62, using 580,422 clear pixels.
- Across my 32 grid cells (31 have raster values), mean NDVI runs from 0.53 to 0.75 and mean elevation from 8.8 m to 30.3 m. Cell 30 has no raster values.
- Lower cells have more flood water: the rank correlation between elevation and flood share is about -0.69 for the November 2024 window and -0.63 for October 2022, and all seven of the lowest cells had flood water in 2024.
- The two cells with recorded spills have mean elevations of 10.7 m and 12.7 m and mean NDVI of 0.60 and 0.66.