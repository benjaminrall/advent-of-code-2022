with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

trees = [[int(height) for height in line] for line in lines]

visible = set()

for y, row in enumerate(trees):
    # Left
    maxHeight = -1
    for x, tree in enumerate(row):
        if tree > maxHeight:
            visible.add((x, y))
            maxHeight = tree
    # Right
    maxHeight = -1
    for x, tree in enumerate(reversed(row)):
        if tree > maxHeight:
            visible.add((len(row) - x - 1, y))
            maxHeight = tree
for x, col in enumerate(zip(*trees)):
    # Top
    maxHeight = -1
    for y, tree in enumerate(col):
        if tree > maxHeight:
            visible.add((x, y))
            maxHeight = tree
    # Bottom
    maxHeight = -1
    for y, tree in enumerate(reversed(col)):
        if tree > maxHeight:
            visible.add((x, len(col) - y - 1))
            maxHeight = tree
print(len(visible))