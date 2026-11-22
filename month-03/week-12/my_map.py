import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio

study = gpd.read_file("data/study_area.gpkg")

with rasterio.open("data/processed/khana_ndvi.tif") as src:
    ndvi = src.read(1, masked=True)
    outline = study.to_crs(src.crs)
    extent = (src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top)

fig, ax = plt.subplots(figsize=(7, 8))
image = ax.imshow(ndvi, cmap="RdYlGn", vmin=-0.2, vmax=0.9, extent=extent)
outline.boundary.plot(ax=ax, color="black", linewidth=1)
fig.colorbar(image, ax=ax, label="NDVI")
ax.set_title("Vegetation index (NDVI), Khana LGA, 19 Dec 2024")
ax.set_axis_off()
fig.savefig("month-03/week-12/my_map.png", dpi=150, bbox_inches="tight")
print("Saved my_map.png")