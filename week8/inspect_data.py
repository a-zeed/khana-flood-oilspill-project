import csv

with open("settlements_near_waterways.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))


def summarise(rows, column):
    values = []
    missing = 0
    for row in rows:
        raw = row[column].strip().replace(",", "")
        if raw == "" or raw.upper() == "NA":
            missing += 1
        else:
            values.append(float(raw))
    return {
        "column": column,
        "count": len(values),
        "missing": missing,
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "mean": round(sum(values) / len(values), 2),
    }


print(summarise(rows, "block_area_sqm"))
print(summarise(rows, "building_count"))