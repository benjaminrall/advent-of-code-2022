import json
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

pairs = []
pair = []
for line in lines:
    if line == "":
        pairs.append(pair)
        pair = []
    else:
        pair.append(json.loads(line))
pairs.append(pair)


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    for x in range(max(len(left), len(right))):
        if x == len(left):
            return 1
        if x == len(right):
            return -1
        c = compare(left[x], right[x])
        if c != 0:
            return c
    return 0

total = 0


for i in range(len(pairs)):
    c = compare(pairs[i][0], pairs[i][1])
    if c == 1:
        total += (i + 1)

print(total)