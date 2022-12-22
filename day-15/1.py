with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

minX = 100000000000000
maxX = -100000000000000
minY = 100000000000000
maxY = -100000000000000
sensors = []
beacons = []

def get_distance(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

detect_y = 2000000

for line in lines:
    sensor, beacon = line.split(":")
    sensor = [int(sensor[sensor.index("x=") + 2: sensor.index(',')]), int(sensor[sensor.index("y=") + 2: ])]
    beacon = [int(beacon[beacon.index("x=") + 2: beacon.index(',')]), int(beacon[beacon.index("y=") + 2: ])]
    distance = get_distance(sensor[0], sensor[1], beacon[0], beacon[1])

    distance_at_y = distance - abs(detect_y - sensor[1])
    sensor_range = [sensor[0] - distance_at_y, sensor[0] + distance_at_y]

    if sensor[0] - distance < minX:
        minX = sensor[0] - distance
    if sensor[0] + distance > maxX:
        maxX = sensor[0] + distance
    if sensor[1] - distance < minY:
        minY = sensor[1] + distance
    if sensor[1] - distance > maxY:
        maxY = sensor[1] + distance

    sensors.append([sensor, sensor_range])
    beacons.append(beacon)

tiles = [0 for _ in range(abs(minX - maxX))]
for sensor in sensors:
    for i in range(sensor[1][0] - minX, sensor[1][1] - minX + 1):
        tiles[i] = 1
for beacon in beacons:
    if beacon[1] == detect_y:
        tiles[beacon[0] - minX] = 0


print(sum(tiles))