with open("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    name = parts[0]
    area = float(parts[1])
    if area > 9:
        size = "large"
    else:
        size = "small"
    print(name, area, size)