import geopandas as gpd

paths = {
    "study area": "data/study_area_utm32.gpkg",
    "settlements": "data/settlements_khana_utm32.gpkg",
    "settlements near waterways": "data/settlements_near_waterways.gpkg",
    "waterway buffer": "data/waterways_buffer_200m.gpkg",
    "waterway lines": "data/waterways_lines_utm32.gpkg",
}

for name, path in paths.items():
    layer = gpd.read_file(path)
    bad = ~layer.is_valid
    print(name, "|", len(layer), "features |", int(bad.sum()), "invalid |", int(layer.is_empty.sum()), "empty")
    if bad.any():
        fixed = layer.make_valid()
        print("    after make_valid:", int((~fixed.is_valid).sum()), "invalid")