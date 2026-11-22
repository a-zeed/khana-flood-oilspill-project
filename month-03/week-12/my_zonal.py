from pathlib import Path
import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

cells = gpd.read_file("data/processed/khana_cells_spills_floods.gpkg", layer="cells")

rasters = {
    "mean_elevation_m": "data/raw/n04_e007_1arc_v3.tif",
    "mean_ndvi": "data/processed/khana_ndvi.tif",
    "mean_ndwi": "data/processed/khana_ndwi.tif",
}

for column, path in rasters.items():
    if not Path(path).exists():
        print("Skipping", column, "- file not found:", path)
        continue
    with rasterio.open(path) as src:
        polygons = cells.to_crs(src.crs)
        means = []
        for geom in polygons.geometry:
            values, _ = mask(src, [geom], crop=True, filled=False)
            means.append(float(values.mean()) if values.count() > 0 else np.nan)
    digits = 1 if column == "mean_elevation_m" else 3
    cells[column] = np.round(means, digits)
    print("Done:", column)

columns = ["cell_id"] + [c for c in rasters if c in cells.columns]
columns += ["spill_count", "flood_2022_pct", "flood_2024_pct"]
table = cells[columns]
table.to_csv("month-03/week-12/khana_cell_zonal_stats.csv", index=False)
print(table.sort_values(columns[1]).to_string(index=False))