
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

with open("input.txt", "r") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]



class Node:
    def __init__(self, x, y):
        self.neighbours = []
        self.x = x
        self.y = y

    def set_neighbours(self, grid, x, y):
        self.neighbours = []
        node_index = ALPHABET.index(grid[y][x])
        if x + 1 < len(grid[0]) and ALPHABET.index(grid[y][x + 1]) - node_index <= 1:
            self.neighbours.append((x + 1, y))
        if x - 1 >= 0 and ALPHABET.index(grid[y][x - 1]) - node_index <= 1:
            self.neighbours.append((x - 1, y))
        if y + 1 < len(grid) and ALPHABET.index(grid[y + 1][x]) - node_index <= 1:
            self.neighbours.append((x, y + 1))
        if y - 1 >= 0 and ALPHABET.index(grid[y - 1][x]) - node_index <= 1:
            self.neighbours.append((x, y - 1))


graph = {}

start_pos = []
end_pos = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'S':
            grid[y][x] = 'a'
            start_pos = (x, y)
        if grid[y][x] == 'E':
            grid[y][x] = 'z'
            end_pos = (x, y)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        graph[(x, y)] = Node(x, y)
        graph[(x, y)].set_neighbours(grid, x, y)
        

paths = []
for y in range(len(grid)):
    for x in range(len(grid[0])):

        if grid[y][x] != 'a':
            continue

        start_pos = (x, y)
        frontier = []
        frontier.append(start_pos)
        visited = set()
        visited.add(start_pos)
        parents = {}
        parents[start_pos] = None
        print(parents)

        final_pos = None

        while len(frontier) > 0:
            current = frontier.pop(0)

            if current == end_pos:
                final_pos = current
                break

            for neighbour in graph[current].neighbours:
                if neighbour not in visited:
                    parents[neighbour] = current
                    frontier.append(neighbour)
                    visited.add(neighbour)
        
        if final_pos is not None:

            path = []
            while parents[final_pos] is not None:
                path.append(final_pos)
                final_pos = parents[final_pos]

            paths.append(len(path))

print(sorted(paths)[0])