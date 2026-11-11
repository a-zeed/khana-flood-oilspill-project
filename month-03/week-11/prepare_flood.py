from pathlib import Path
import geopandas as gpd

study = gpd.read_file("data/study_area.gpkg")
study_utm = study.to_crs(epsg=32632)
khana_km2 = study_utm.area.sum() / 1_000_000

gdb_2022 = Path(r"C:\Users\zeema\Downloads\FL20221019NGA\FL20221019NGA.gdb")
shp_2024 = Path(r"C:\Users\zeema\Downloads\FL2024\FL20240902NGA_SHP")

layers = {
    "flood_2022": (gdb_2022, "VIIRS_20221013_20221017_MaximumFloodWaterExtent_Nigeria"),
    "permanent_2022": (gdb_2022, "VIIRS_20221013_20221017_PermanentWater_Nigeria"),
    "cloud_2022": (gdb_2022, "VIIRS_20221013_20221017_CloudObstruction_Nigeria"),
    "flood_2024": (shp_2024 / "VIIRS_20241109_20241113_MaximumFloodExtent_NGA.shp", None),
    "cloud_2024": (shp_2024 / "VIIRS_20241109_20241113_CloudObstruction_NGA.shp", None),
}

parts = {}
for name, (source, layer) in layers.items():
    raw = gpd.read_file(source, layer=layer, mask=study)
    parts[name] = raw.to_crs(epsg=32632).clip(study_utm)
    area = parts[name].area.sum() / 1_000_000
    print(f"{name}: {area:.2f} km2 ({area / khana_km2 * 100:.1f}% of Khana)")

for name in ("flood_2022", "flood_2024"):
    if parts[name].empty:
        print(name, "has no flood water inside Khana")
    else:
        parts[name].to_file(f"data/processed/khana_{name}.gpkg", layer=name)
        print("Saved data/processed/khana_" + name + ".gpkg")