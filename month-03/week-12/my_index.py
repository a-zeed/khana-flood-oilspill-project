import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

folder = "data/raw/landsat/"
scene = "LC09_L2SP_188057_20241219_20241220_02_T1"

study = gpd.read_file("data/study_area.gpkg")


def read_band(name):
    with rasterio.open(f"{folder}{scene}_{name}.TIF") as src:
        area = study.to_crs(src.crs)
        raw, transform = mask(src, area.geometry, crop=True, nodata=0)
        profile = {
            "driver": "GTiff", "dtype": "float32", "count": 1, "nodata": -9999,
            "crs": src.crs, "transform": transform,
            "height": raw.shape[1], "width": raw.shape[2],
        }
    return raw[0], profile


def scale(raw):
    return raw.astype("float32") * 0.0000275 - 0.2


def normalised_difference(a, b, valid):
    result = np.full(a.shape, -9999, dtype="float32")
    total = a + b
    ok = valid & (total != 0)
    result[ok] = (a[ok] - b[ok]) / total[ok]
    return result, ok


green_raw, profile = read_band("SR_B3")
red_raw, _ = read_band("SR_B4")
nir_raw, _ = read_band("SR_B5")
qa, _ = read_band("QA_PIXEL")

inside = qa > 1
cloudy = (qa & 30) > 0
cloud_pct = round(float(cloudy[inside].mean()) * 100, 1)
print("Cloud, shadow or cirrus over Khana:", cloud_pct, "percent")

valid = (green_raw > 0) & (red_raw > 0) & (nir_raw > 0) & ~cloudy
print("Clear pixels used:", int(valid.sum()))

green, red, nir = scale(green_raw), scale(red_raw), scale(nir_raw)

ndvi, ndvi_ok = normalised_difference(nir, red, valid)
ndwi, ndwi_ok = normalised_difference(green, nir, valid)

for name, result, ok in (("NDVI", ndvi, ndvi_ok), ("NDWI", ndwi, ndwi_ok)):
    low = round(float(result[ok].min()), 3)
    high = round(float(result[ok].max()), 3)
    print(name, "range:", low, "to", high)
    print(name, "mean:", round(float(result[ok].mean()), 3))
    with rasterio.open(f"data/processed/khana_{name.lower()}.tif", "w", **profile) as dst:
        dst.write(result, 1)
    print("Saved data/processed/khana_" + name.lower() + ".tif")