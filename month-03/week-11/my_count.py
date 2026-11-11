import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import box

study = gpd.read_file("data/study_area_utm32.gpkg")
outline = study.geometry.iloc[0]

table = pd.read_csv("data/raw/khana_spills_api.csv")
spills = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326",
).to_crs(study.crs)
spills_in = spills[spills.within(outline)]
print("Spills in the table:", len(spills), "| inside the Khana outline:", len(spills_in))

minx, miny, maxx, maxy = study.total_bounds
size = 5000
cells = [
    box(x, y, x + size, y + size)
    for x in np.arange(minx, maxx, size)
    for y in np.arange(miny, maxy, size)
]
grid = gpd.GeoDataFrame({"cell_id": range(len(cells))}, geometry=cells, crs=study.crs)
grid = grid[grid.intersects(outline)].reset_index(drop=True)
grid["geometry"] = grid.intersection(outline)
grid["cell_km2"] = grid.area / 1_000_000
print("Grid cells:", len(grid))

joined = gpd.sjoin(
    spills_in[["id", "geometry"]], grid[["cell_id", "geometry"]],
    how="inner", predicate="within",
)
counts = joined.groupby("cell_id").size().rename("spill_count").reset_index()
grid = grid.merge(counts, on="cell_id", how="left")
grid["spill_count"] = grid["spill_count"].fillna(0).astype(int)
print("Total counted:", grid["spill_count"].sum(), "of", len(spills_in))

for year in ("2022", "2024"):
    flood = gpd.read_file(f"data/processed/khana_flood_{year}.gpkg")
    pieces = gpd.overlay(grid[["cell_id", "geometry"]], flood[["geometry"]], how="intersection")
    pieces["flood_km2"] = pieces.area / 1_000_000
    per_cell = pieces.groupby("cell_id")["flood_km2"].sum().reset_index()
    grid = grid.merge(per_cell, on="cell_id", how="left")
    grid["flood_km2"] = grid["flood_km2"].fillna(0)
    grid[f"flood_{year}_pct"] = (grid["flood_km2"] / grid["cell_km2"] * 100).round(1)
    grid[f"flooded_{year}"] = np.where(grid[f"flood_{year}_pct"] > 0, "yes", "no")
    grid = grid.drop(columns="flood_km2")

either_year = (grid["flooded_2022"] == "yes") | (grid["flooded_2024"] == "yes")
grid["spill_and_flood"] = np.where((grid["spill_count"] > 0) & either_year, "yes", "no")

columns = ["cell_id", "cell_km2", "spill_count", "flood_2022_pct", "flooded_2022",
           "flood_2024_pct", "flooded_2024", "spill_and_flood"]
out = grid[columns].copy()
out["cell_km2"] = out["cell_km2"].round(2)
out.to_csv("data/processed/khana_cells_spills_floods.csv", index=False)
grid.to_file("data/processed/khana_cells_spills_floods.gpkg", layer="cells")
print(out.sort_values("spill_count", ascending=False).head(6).to_string(index=False))
print("Cells with a spill:", int((grid["spill_count"] > 0).sum()),
      "| flooded 2022:", int((grid["flooded_2022"] == "yes").sum()),
      "| flooded 2024:", int((grid["flooded_2024"] == "yes").sum()),
      "| spill and flood:", int((grid["spill_and_flood"] == "yes").sum()))

top = max(grid["flood_2022_pct"].max(), grid["flood_2024_pct"].max(), 1)
fig, axes = plt.subplots(1, 2, figsize=(12, 7))
for ax, year in zip(axes, ("2022", "2024")):
    grid.plot(ax=ax, column=f"flood_{year}_pct", cmap="Blues", edgecolor="#999999",
              linewidth=0.4, legend=True, vmin=0, vmax=top)
    study.boundary.plot(ax=ax, color="#037E8E", linewidth=1.2)
    spills_in.plot(ax=ax, color="#C0392B", markersize=30)
    ax.set_title(f"Flood water {year} (% of cell)", fontsize=11)
    ax.set_axis_off()
fig.suptitle("Red dots: recorded oil spills inside Khana LGA", fontsize=12)
fig.savefig("month-03/week-11/my_count_map.png", dpi=150, bbox_inches="tight")
print("Map saved")