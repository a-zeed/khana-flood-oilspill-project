import csv

def read_rows(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip().replace(",", "")
        if raw == "" or raw.upper() == "NA":
            continue
        values.append(float(raw))
    return values

def summarise(values):
    if len(values) == 0:
        return {"count": 0}
    return {
        "count": len(values),
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "mean": round(sum(values) / len(values), 2),
    }


def summarise_all(rows, columns):
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report


rows = read_rows("settlements_near_waterways.csv")
report = summarise_all(rows, ["block_area_sqm", "building_count"])
for column, stats in report.items():
    print(f"{column}: count {stats['count']},  smallest {stats['min']}, largest {stats['max']}, average {stats['mean']}")