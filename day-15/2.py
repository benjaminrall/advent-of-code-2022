import numpy as np

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

minX = 100000000000000
maxX = -100000000000000
minY = 100000000000000
maxY = -100000000000000
sensors = []


def get_distance(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

detect_y = 2000000
maxSearch = 4000000

possible_rows = []

for line in lines:
    sensor, beacon = line.split(":")
    sensor = [int(sensor[sensor.index("x=") + 2: sensor.index(',')]), int(sensor[sensor.index("y=") + 2: ])]
    beacon = [int(beacon[beacon.index("x=") + 2: beacon.index(',')]), int(beacon[beacon.index("y=") + 2: ])]
    distance = get_distance(sensor[0], sensor[1], beacon[0], beacon[1])
    sensors.append([sensor, beacon, distance])
    
def valid(x, y):
    if x < 0 or x > maxSearch or y < 0 or y > maxSearch:
        #print(x,y)
        return False
    
    for s2, _, d2 in sensors:
        if get_distance(s2[0], s2[1], x, y) <= d2:
            print(s2)
            return False
    
    return True


L = len(sensors)
i = 0
for sensor, beacon, distance in sensors:
    for x in range(sensor[0] - distance - 1, sensor[0] + distance + 2):
        for ym in range(-1, 2, 2):
            y = sensor[1] + (distance + 1 - abs(x)) * ym
            if valid(x, y):
                print(x, y)
                exit()
    i += 1
    print(f"{i}/{L} complete")