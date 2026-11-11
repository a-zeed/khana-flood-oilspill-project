import geopandas as gpd

study = gpd.read_file("data/study_area.gpkg")
lines = gpd.read_file("data/waterways_lines_clipped.gpkg")

print("Study area CRS:", study.crs)
print("Waterway lines CRS:", lines.crs)
print("Suggested UTM:", study.estimate_utm_crs())

study_utm = study.to_crs(epsg=32632)
lines_utm = lines.to_crs(epsg=32632)

print("Study area:", round(study_utm.area.sum() / 1_000_000, 2), "km2")
print("Waterway length:", round(lines_utm.length.sum() / 1000, 2), "km")