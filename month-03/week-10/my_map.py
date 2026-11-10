import geopandas as gpd
import matplotlib.pyplot as plt

study = gpd.read_file("data/study_area_utm32.gpkg")
settlements = gpd.read_file("data/settlements_khana_utm32.gpkg")
near = gpd.read_file("data/settlements_near_waterways.gpkg")
lines = gpd.read_file("data/waterways_lines_utm32.gpkg")
points = gpd.read_file("data/waterways_points_utm32.gpkg")

layers = {
    "study area": study,
    "settlements": settlements,
    "near waterways": near,
    "waterway lines": lines,
    "waterway points": points,
}
for name, layer in layers.items():
    print(name, len(layer), layer.crs)

fig, ax = plt.subplots(figsize=(8, 9))
study.plot(ax=ax, color="#F4F8F8", edgecolor="#037E8E", linewidth=1.5)
settlements.plot(ax=ax, color="#BDBDBD", label="Settlements")
near.plot(ax=ax, color="#C0392B", label="Settlements near waterways")
lines.plot(ax=ax, color="#1F78B4", linewidth=0.8, label="Waterways")
points.plot(ax=ax, color="#094923", markersize=30, label="Waterway points")
ax.set_title("Khana LGA: settlements near waterways")
ax.set_axis_off()
ax.legend(loc="lower left", fontsize=8)

fig.savefig("month-03/week-10/my_map.png", dpi=150, bbox_inches="tight")
print("Map saved")