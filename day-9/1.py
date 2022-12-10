with open("input.txt", "r") as f:
    lines = [line.strip().split(" ") for line in f.readlines()]
    lines = [[line[0], int(line[1])] for line in lines]

visited_tail = set()
head_pos = [0, 0]
tail_pos = (0, 0)
visited_tail.add(tail_pos)

for line in lines:
    instruction = line[0]
    for _ in range(line[1]):
        if instruction == 'R':
            head_pos[0] += 1
        if instruction == 'L':
            head_pos[0] -= 1
        if instruction == 'U':
            head_pos[1] += 1
        if instruction == 'D':
            head_pos[1] -= 1
        dx = head_pos[0] - tail_pos[0]
        dy = head_pos[1] - tail_pos[1]
        if dy == 0 and dx == 2:
            tail_pos = (tail_pos[0] + 1, tail_pos[1])
        elif dy == 0 and dx == -2:
            tail_pos = (tail_pos[0] - 1, tail_pos[1])
        elif dy == 2 and dx == 0:
            tail_pos = (tail_pos[0], tail_pos[1] + 1)
        elif dy == -2 and dx == 0:
            tail_pos = (tail_pos[0], tail_pos[1] - 1)
        elif dx >= 1 and dy >= 1:
            tail_pos = (tail_pos[0] + 1, tail_pos[1] + 1)
        elif dx <= -1 and dy >= 1:
            tail_pos = (tail_pos[0] - 1, tail_pos[1] + 1)
        elif dx <= -1 and dy <= -1:
            tail_pos = (tail_pos[0] - 1, tail_pos[1] - 1)
        elif dx >= 1 and dy <= -1:
            tail_pos = (tail_pos[0] + 1, tail_pos[1] - 1)

        visited_tail.add(tail_pos)
print(visited_tail)
print(len(visited_tail))