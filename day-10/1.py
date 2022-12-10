with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

state = {1: 1}

X = 1
cycle = 1
for line in lines:
    if line.startswith("noop"):
        cycle += 1
    else:
        add_command = int(line.split(" ")[1])
        cycle += 2
        X += add_command
        state[cycle] = X

m = 0
for i in range(1, sum([2 if command.startswith("add") else 1 for command in lines]) + 2):
    if i in state:
        m = state[i]
    else:
        state[i] = m

print(state[20] * 20 + state[60] * 60 + state[100] * 100 + state[140] * 140 + state[180] * 180 + state[220] * 220)