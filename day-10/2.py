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
for i in range(1, 241):
    if i in state:
        m = state[i]
    else:
        state[i] = m

output_image = ""

crt_pos = 0
for cycle in range(1, 241):
    if crt_pos >= 40:
        crt_pos -= 40
        output_image += "\n"
    if abs(state[cycle] - crt_pos) <= 1:
        output_image += "#"
    else:
        output_image += "."
    crt_pos += 1

print(output_image)