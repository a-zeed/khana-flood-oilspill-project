Project CRS: EPSG:32632 (UTM zone 32N, Khana LGA)

# Data notes

## GRID3 NGA – Operational LGA Boundaries
- Dataset name: GRID3 NGA – Operational LGA Boundaries
- Version/date: released March 2021
- Source link: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about
- Feature count: 774 (one per LGA, nationwide — matches Nigeria's official LGA count, good sanity check)
- Geometry type: Polygon (MultiPolygon)
- Key columns: lganame, lgacode, statename, statecode, source, amapcode, globalid, uniq_id, timestamp, editor
- Note: Khana appears as one row within this nationwide file (statename = Rivers). Will need to filter/select Khana specifically before clipping other layers to it in Week 3.
- CRS as downloaded: EPSG:4326 (WGS 84) — will need reprojecting before any area/distance calculations.

## OSM Waterways (lines) — Khana LGA, via QuickOSM
- Source: OpenStreetMap, extracted via QuickOSM (key: waterway) for Khana LGA extent
- Extracted: 5 September 2026
- Feature count: 76
- Geometry type: Line
- Key columns: full_id, osm_id, osm_type, waterway (river/stream), tunnel, layer, name, GNS:dsg_string, GNS:dsg_code, GNS:id
- Gaps noticed: most features have a NULL name — only a handful of named waterways (e.g. Imo River, River Uyin, Afa Creek). Most streams/rivers in this area are mapped but not individually labelled, so any analysis using waterway names will only cover a small fraction of the actual network.

## GRID3 NGA – Settlement Extents v4.1
- Dataset name: GRID3 NGA – Settlement Extents v4.1
- Version/date: August 2026
- Source link: https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about
- Feature count: 2,546,560 (nationwide, not yet clipped to Khana LGA)
- Geometry type: Polygon (MultiPolygon)
- Key columns: block_id, country, iso3, block_area_sqm, block_perimeter, building_count, building_area_min, building_area_max, building_area_sum, building_area_median
- Note: this is building-block level data rather than one row per named settlement — each polygon represents a cluster of buildings, with stats on how many buildings and how much building area it contains. Useful for identifying built-up areas, but does not carry settlement names directly.
- CRS as downloaded: EPSG:3857 (Web Mercator) — will need reprojecting to a proper UTM zone (32631 or 32632) before any distance/area analysis, per Week 3.

## OSM Waterways (points) — Khana LGA, via QuickOSM
- Source: OpenStreetMap, extracted via QuickOSM (key: waterway) for Khana LGA extent
- Extracted: 5 September 2026
- Feature count: 4
- Geometry type: Point
- Key columns: full_id, osm_id, osm_type, ford
- Note: these are river/stream fords (ford=yes) — road crossings over waterways with no bridge — not water points or springs as initially expected. Very small sample size (4), so likely under-mapped in this area; not enough to draw conclusions about ford locations generally, but worth flagging as points that may flood or become impassable first.

## Rasters (Week 12)

- data/raw/n04_e007_1arc_v3.tif: SRTM 1 Arc-Second Global elevation, tile N04E007, version 3, from USGS EarthExplorer, downloaded 2026-11-21. GeoTIFF, int16, EPSG:4326, 3601 x 3601, about 30 m cells, nodata -32767. Not committed.
- data/raw/landsat/LC09_L2SP_188057_20241219_20241220_02_T1_SR_B3.TIF, _SR_B4.TIF, _SR_B5.TIF and _QA_PIXEL.TIF: Landsat 9 Collection 2 Level-2 surface reflectance and quality band, acquired 2024-12-19, land cloud cover 10.89 percent, from USGS EarthExplorer. Not committed.
- data/processed/khana_ndvi.tif and khana_ndwi.tif: made by my_index.py from those bands, cut to the Khana outline and cloud masked. Not committed.
- data/raw/dem.tif and the Landsat bands for scene LC09_L2SP_191055_20260115_20260117_02_T1: the Ibadan North teaching rasters from the starter data. Not committed.
- Other Landsat files in data/raw/landsat (scenes from 23 January 2026 and 31 July 2025) were downloaded while choosing a scene and are not used. Not committed.