with open("input.txt", "r") as f:
    lines = [[int(c) for c in line.strip().split(",")] for line in f.readlines()]

x_bounds = [100, -100]
y_bounds = [100, -100]
z_bounds = [100, -100]
for pos in lines:
    x_bounds[0] = min(x_bounds[0], pos[0])
    y_bounds[0] = min(y_bounds[0], pos[1])
    z_bounds[0] = min(z_bounds[0], pos[2])
    x_bounds[1] = max(x_bounds[1], pos[0])
    y_bounds[1] = max(y_bounds[1], pos[1])
    z_bounds[1] = max(z_bounds[1], pos[2])
print(x_bounds, y_bounds, z_bounds)

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

