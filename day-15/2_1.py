import numpy as np

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def get_distance(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

maxSearch = 4000000
possible_rows = [[] for _ in range(maxSearch)]
sensors = []
for line in lines:
    sensor, beacon = line.split(":")
    sensor = [int(sensor[sensor.index("x=") + 2: sensor.index(',')]), int(sensor[sensor.index("y=") + 2: ])]
    beacon = [int(beacon[beacon.index("x=") + 2: beacon.index(',')]), int(beacon[beacon.index("y=") + 2: ])]
    distance = get_distance(sensor[0], sensor[1], beacon[0], beacon[1])
    sensors.append([sensor, beacon, distance])

L = len(sensors)
i = 0
for s, b, r in sensors:
    for dy in range(-r, r+1):
        y = s[1] + dy
        if y < 0 or y >= maxSearch:
            continue
        dx = abs(dy) - r
        x0 = s[0] + dx
        x1 = s[0] - dx
        possible_rows[y].append([min(x0, x1), max(x0, x1)])
    i += 1
    print(f"{i}/{L} complete")

print("Calculated rows")
for y, row in enumerate(possible_rows):
    x = np.full((maxSearch), 1)
    for slice in row:
        x[max(slice[0], 0):min(slice[1]+1,maxSearch)] = 0
    sols = np.where(x == 1)
    if len(sols[0]) > 0:
        print(sols[0][0] * 4000000 + y)
    if y % 1000 == 0:
        print(f"{y} complete")
