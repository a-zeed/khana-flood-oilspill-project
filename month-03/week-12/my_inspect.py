
import numpy as np
import rasterio

paths = {
    "DEM (SRTM)": "data/raw/n04_e007_1arc_v3.tif",
    "NDVI": "data/processed/khana_ndvi.tif",
    "NDWI": "data/processed/khana_ndwi.tif",
}

for name, path in paths.items():
    with rasterio.open(path) as src:
        print("\n---", name, "---")
        print("Width x height:", src.width, "x", src.height)
        print("Bands:", src.count)
        print("Data type:", src.dtypes)
        print("CRS:", src.crs)
        print("Pixel size:", src.res)
        print("Bounds:", src.bounds)
        print("Nodata:", src.nodata)

        span_x = src.width * src.res[0]
        span_y = src.height * src.res[1]
        full_x = src.bounds.right - src.bounds.left
        full_y = src.bounds.top - src.bounds.bottom
        print("Width check passes:", abs(span_x - full_x) < 1e-6)
        print("Height check passes:", abs(span_y - full_y) < 1e-6)

        data = src.read(1, masked=True)
        print("Minimum:", round(float(data.min()), 3))
        print("Maximum:", round(float(data.max()), 3))
        print("Mean:", round(float(data.mean()), 3))