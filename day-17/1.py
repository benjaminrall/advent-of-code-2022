import copy


COLUMNS = [[0], [0], [0], [0], [0], [0], [0]]


class Rock:
    def __init__(self, width, shape) -> None:
        self.width = width
        self.shape = shape
        self.x = 2
        self.height = 4
        self.settled = False

    def setup(self, height):
        self.x = 2
        self.height = height

    def settle(self):
        for i, col in enumerate(self.shape):
            COLUMNS[self.x + i].extend([n for n in range(self.height + col[0], self.height + col[1] + 1)]) 
        self.settled = True

    def overlaps(self):
        for i, col in enumerate(self.shape):
            for j in range(col[0], col[1] + 1):
                if self.height + j in COLUMNS[self.x + i]:
                    return True
        return False

    def moveDown(self):
        self.height -= 1
        if self.overlaps():
            self.height += 1
            self.settle()

    
    def moveLeft(r):
        if r.x == 0:
            return
        r.x -= 1
        if r.overlaps():
            r.x += 1
    
    def moveRight(r):
        if r.x == 7 - r.width:
            return
        r.x += 1
        if r.overlaps():
            r.x -= 1


horizontal = Rock(4, [[0, 0], [0, 0], [0, 0], [0, 0]])
plus = Rock(3, [[1, 1], [0, 2], [1, 1]])
el = Rock(3, [[0, 0], [0, 0], [0, 2]])
vertical = Rock(1, [[0, 3]])
square = Rock(2, [[0, 1], [0, 1]])
rocks = [horizontal, plus, el, vertical, square]

rocks_spawned = 0
max_rocks = 2022
current_rock = None
next_push = 0
next_rock = 0
next_action = False # 0 = push, 1 = fall

with open("input.txt", "r") as f:
    push = [Rock.moveLeft if c == '<' else Rock.moveRight for c in f.read()]

while rocks_spawned <= max_rocks:
    if current_rock is None:
        current_rock = copy.deepcopy(rocks[next_rock])
        next_rock = (next_rock + 1) % 5
        current_rock.setup(max([col[-1] for col in COLUMNS]) + 4)
        rocks_spawned += 1
        continue
    if not next_action:
        push[next_push](current_rock)
        next_push = (next_push + 1) % len(push)
    else:
        current_rock.moveDown()
        if current_rock.settled:
            current_rock = None
    next_action = not next_action

print(max([col[-1] for col in COLUMNS]))