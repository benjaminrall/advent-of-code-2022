import json

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

packets = [[[2]], [[6]]]
for line in lines:
    if line == "":
        continue
    packets.append(json.loads(line))

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    for x in range(max(len(left), len(right))):
        if x == len(left):
            return True
        if x == len(right):
            return False
        c = compare(left[x], right[x])
        if c is not None:
            return c
    return None


sorted_packets = []
while len(packets) > 0:
    best_i = 0
    minimum = packets[0]
    for i in range(1, len(packets)):
        if not compare(minimum, packets[i]):
            minimum = packets[i]
            best_i = i
    sorted_packets.append(packets.pop(best_i))

print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))