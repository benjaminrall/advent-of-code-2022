with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

trees = [[int(height) for height in line] for line in lines]


def scenic_score(x, y, trees):
    left = 0
    right = 0
    up = 0
    down = 0
    # left
    for i in range(1, x + 1):
        left += 1
        tree = trees[y][x - i]
        if tree >= trees[y][x]:
            break
    # right
    for i in range(1, len(trees[0]) - x):
        right += 1
        tree = trees[y][x + i]
        if tree >= trees[y][x]:
            break
    # up
    for i in range(1, y + 1):
        up += 1
        tree = trees[y - i][x]
        if tree >= trees[y][x]:
            break
    # down
    for i in range(1, len(trees) - y):
        down += 1
        tree = trees[y + i][x]
        if tree >= trees[y][x]:
            break
    return left * right * up * down

highest = 0
for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[0]) - 1):
        score = scenic_score(x, y, trees)
        if score > highest:
            highest = score

print(highest)