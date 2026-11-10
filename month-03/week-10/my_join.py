import pandas as pd
import geopandas as gpd

settlements = gpd.read_file("data/settlements_khana_utm32.gpkg", layer="settlements_khana_utm32")
table = pd.read_csv("week8/settlements_near_waterways.csv")

print("Settlements in the layer:", len(settlements))
print("Rows in the table:", len(table))
print("Unique block_id in the table:", table["block_id"].nunique())

table["near_waterway"] = "yes"
joined = settlements.merge(table[["block_id", "near_waterway"]], on="block_id", how="left")

matched = joined["near_waterway"].notna().sum()
print("Matched on first try:", matched, "of", len(table))
print("Rows after the join:", len(joined))

joined["near_waterway"] = joined["near_waterway"].fillna("no")
print(joined["near_waterway"].value_counts())