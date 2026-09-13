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

