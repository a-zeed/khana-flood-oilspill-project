import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

original = gpd.read_file("data/waterways_points_clipped.gpkg")
print("Original points:", len(original), original.crs)

table = original.drop(columns="geometry")
table["longitude"] = original.geometry.x
table["latitude"] = original.geometry.y
table.to_csv("data/processed/waterway_points.csv", index=False)
print(table)

table = pd.read_csv("data/processed/waterway_points.csv")
points = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326",
)
points.to_file("data/processed/waterway_points.gpkg", layer="waterway_points")

study = gpd.read_file("data/study_area.gpkg")
inside = points.within(study.geometry.iloc[0])
print("Points inside the study area:", inside.sum(), "of", len(points))

fig, ax = plt.subplots(figsize=(7, 8))
study.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
points.plot(ax=ax, color="#094923", markersize=40)
ax.set_title("Waterway points over the Khana study area")
ax.set_axis_off()
fig.savefig("month-03/week-10/my_points_check.png", dpi=150, bbox_inches="tight")
print("Map saved")