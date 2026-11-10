import geopandas as gpd

path = "data/settlements_near_waterways.gpkg"

print(gpd.list_layers(path))

layer = gpd.read_file(path, layer="settlements_khana_utm32")

print(layer.head())
print("Rows and columns:", layer.shape)
print(layer.geom_type.value_counts())
print("CRS:", layer.crs)
print("Bounds:", layer.total_bounds)