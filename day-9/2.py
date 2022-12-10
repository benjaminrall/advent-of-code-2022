with open("input.txt", "r") as f:
    lines = [line.strip().split(" ") for line in f.readlines()]
    lines = [[line[0], int(line[1])] for line in lines]

class Knot:
    def __init__(self) -> None:
        self.pos = (0, 0)
        self.tail: Knot = None
    
    def add(self, x, y):
        self.pos = (self.pos[0] + x, self.pos[1] + y)
    
    def update_tail(self):
        if self.tail is not None:
            dx = self.pos[0] - self.tail.pos[0]
            dy = self.pos[1] - self.tail.pos[1]
            d = abs(dx) + abs(dy)
            if dy == 0 and dx == 2:
                self.tail.add(1, 0)
            elif dy == 0 and dx == -2:
                self.tail.add(-1, 0)
            elif dy == 2 and dx == 0:
                self.tail.add(0, 1)
            elif dy == -2 and dx == 0:
                self.tail.add(0, -1)
            elif dx >= 1 and dy >= 1 and d >= 3:
                self.tail.add(1, 1)
            elif dx <= -1 and dy >= 1 and d >= 3:
                self.tail.add(-1, 1)
            elif dx <= -1 and dy <= -1 and d >= 3:
                self.tail.add(-1, -1)
            elif dx >= 1 and dy <= -1 and d >= 3:
                self.tail.add(1, -1)
            #print(f"Updating tail {dx} {dy}")
            self.tail.update_tail()

visited = set()
knots = [Knot() for _ in range(10)]
for i in range(len(knots) - 1):
    knots[i].tail = knots[i + 1]
visited.add(knots[-1].pos)

for line in lines:
    instruction = line[0]
    for _ in range(line[1]):
        if instruction == 'R':
            knots[0].add(1, 0)
        if instruction == 'L':
            knots[0].add(-1, 0)
        if instruction == 'U':
            knots[0].add(0, 1)
        if instruction == 'D':
            knots[0].add(0, -1)
        knots[0].update_tail()
        visited.add(knots[-1].pos)
print(visited)
print(len(visited))