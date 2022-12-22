import sys
import random

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


print(distances)

def search_together(depth1, depth2, current1, current2, path, to_explore):
    if depth1 < 0 or depth2 < 0:
        return 0
    
    removed1 = False
    removed2 = False
    if current1 in to_explore:
        i1 = to_explore.index(current1)
        to_explore.remove(current1)
        removed1 = True

    if current1 != current2 and current2 in to_explore:
        i2 = to_explore.index(current2)
        to_explore.remove(current2)
        removed2 = True

    best = path
    for key1 in to_explore:
        for key2 in to_explore:
            if key1 != key2:
                distance1 = distances[current1][key1] + 1
                distance2 = distances[current2][key2] + 1
                best = max(search_together(
                    (depth1 - distance1) if depth1 != 0 else 0,
                    (depth2 - distance2) if depth2 != 0 else 0,
                    key1 if depth1 != 0 else current1,
                    key2 if depth2 != 0 else current2,
                    path + ((flows[key1] * (depth1 - distance1)) if depth1 != 0 else 0) 
                         + ((flows[key2] * (depth2 - distance2)) if depth2 != 0 else 0),
                    to_explore
                ), best)

    if removed2:
        to_explore.insert(i2, current2)
    if removed1:
        to_explore.insert(i1, current1)

    print(best)
    return best
    
print("Started search.")
sys.setrecursionlimit(1000000)
x = [key for key in distances]
random.shuffle(x)
print(search_together(26, 26, 'AA', 'AA', 0, x))