with open("input.txt", "r") as f:
    lines = [[int(c) for c in line.strip().split(",")] for line in f.readlines()]


def cube_sides(p):
    return set([
        (p[0] + 0.5, p[1], p[2]),
        (p[0] - 0.5, p[1], p[2]),
        (p[0], p[1] + 0.5, p[2]),
        (p[0], p[1] - 0.5, p[2]),
        (p[0], p[1], p[2] + 0.5),
        (p[0], p[1], p[2] - 0.5),
    ])

sides = set()
for pos in lines:
    s = cube_sides(pos)
    sides = s.difference(sides).union(sides.difference(s))
print(len(sides))
        