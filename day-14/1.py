with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

map = [['.' for _ in range(1000)] for _ in range(500)]
for line in lines:
    steps = [[int(p)for p in c.split(",")] for c in line.split(" -> ")]
    for step in range(len(steps) - 1):
        s1 = steps[step]
        s2 = steps[step + 1]
        for y in range(min(s1[1], s2[1]), max(s1[1], s2[1]) + 1):
            for x in range(min(s1[0], s2[0]), max(s1[0], s2[0]) + 1):
                map[y][x] = '#'

source = [500, 0]

running = True
sand_settled = 0
sand = None
while running:
    if sand is None:
        sand = source.copy()
    else:
        if sand[1] + 1 >= 500 or sand[0] - 1 < 0 or sand[0] + 1 >= 1000:
            running = False
        elif map[sand[1] + 1][sand[0]] == '.':
            sand = [sand[0], sand[1] + 1]
        elif map[sand[1] + 1][sand[0] - 1] == '.':
            sand = [sand[0] - 1, sand[1] + 1]
        elif map[sand[1] + 1][sand[0] + 1] == '.':
            sand = [sand[0] + 1, sand[1] + 1]
        else:
            sand_settled += 1
            map[sand[1]][sand[0]] = 'o'
            sand = None
print(sand_settled)