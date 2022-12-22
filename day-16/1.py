with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

flows = {}
connections = {}
start = 'AA'

for line in lines:
    vi = line.index("Valve ") + 6
    valve = line[vi:vi+2]
    fi = [line.index("rate=") + 5, line.index(";")]
    flows[valve] = int(line[fi[0]:fi[1]])
    ci = line.index("valve") + 6
    try:
        line.index("valves")
        ci += 1
    except:
        pass
    connections[valve] = (line[ci:].split(", ")) 

def distance(node1, node2):
    frontier = [(node1, 0)]
    visited = set([node1])

    while len(frontier) > 0:
        current, d = frontier.pop(0)

        if current == node2:
            return d
        
        for connection in connections[current]:
            if connection not in visited:
                frontier.append((connection, d + 1))
                visited.add(connection)
    
    return -1

def search(depth, current, path, to_explore, display =False):
    if depth == 0:
        return path
    elif depth < 0:
        return 0

    i = to_explore.index(current)    
    to_explore.remove(current)

    best = path
    for key in to_explore:
        if display:
            print(key)
        distance = distances[current][key] + 1
        best = max(search(depth - distance, key, path + flows[key] * (depth - distance), to_explore), best)

    to_explore.insert(i, current)

    return best

best = 0

distances = { key: {} for key in flows if flows[key] != 0}
distances['AA'] = {}

for key1 in distances:
    for key2 in distances:
        if key1 != key2:
            distances[key1][key2] = distance(key1, key2)

    
print("Started search.")
print(search(30, 'AA', 0, [key for key in distances], True))