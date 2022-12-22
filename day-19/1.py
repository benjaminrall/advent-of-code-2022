with open("inpu.txt","r") as f:
    blueprints = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

def max_val(m, c, n):
    return c + m * n

def turns_until_greater(m, c, n):
    i = 0
    while c + m * i < n:
        i += 1
    return i

def simulate(blueprint):
    orebots = 1
    claybots = 0
    obbots = 0
    geobots = 0
    current_gen = 0
    ore = 0
    clay = 0
    ob = 0
    geo = 0
    creating_bot = 100
    for _ in range(24):
        if current_gen == 3
        


        if current_gen <= 3 and ore >= blueprint[5] and ob >= blueprint[6]:
            creating_bot = 3
            current_gen = 3
            ore -= blueprint[5]
            ob -= blueprint[6]
        elif current_gen <= 2 and ore >= blueprint[3] and clay >= blueprint[4]:
            creating_bot = 2
            current_gen = 2
            ore -= blueprint[3]
            clay -= blueprint[4]
        elif current_gen <= 1 and ore >= blueprint[2]:
            creating_bot = 1
            current_gen = 1
            ore -= blueprint[2]
        elif current_gen == 0 and ore >= blueprint[1]:
            creating_bot = 0
            ore -= blueprint[1]
        
        ore += orebots
        clay += claybots
        ob += obbots
        geo += geobots
        print(f"You now have {ore} ore {clay} clay {ob} ob {geo} geo, creating bot {creating_bot}")

        if creating_bot == 0:
            orebots += 1
        elif creating_bot == 1:
            claybots += 1
        elif creating_bot == 2:
            obbots += 1
        elif creating_bot == 3:
            geobots += 1

        creating_bot = 100
    return geo


print(simulate(blueprints[0]))