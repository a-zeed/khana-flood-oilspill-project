import pandas as pd
import geopandas as gpd

study = gpd.read_file("data/study_area_utm32.gpkg")
lines = gpd.read_file("data/waterways_lines_utm32.gpkg")

table = pd.read_csv("data/raw/khana_spills_api.csv")
spills = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326",
).to_crs(study.crs)
spills = spills[spills.within(study.geometry.iloc[0])]
print("Spills inside Khana:", len(spills))

nearest = gpd.sjoin_nearest(
    spills[["id", "incidentdate", "sitelocationname", "geometry"]],
    lines[["full_id", "geometry"]],
    how="left",
    distance_col="distance_m",
)
nearest["distance_m"] = nearest["distance_m"].round(0)
print(nearest[["id", "incidentdate", "sitelocationname", "full_id", "distance_m"]].to_string(index=False))
print("Rows:", len(nearest), "for", len(spills), "spills")
