with open("input.txt", "r") as f:
    lines = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
    
i = 0
stack_building = []
while lines[i] != '':
    stack_building.append(lines[i])
    i += 1
stacks_n = int([x for x in stack_building[-1].split(' ') if x != ''][-1])
stacks = [[] for _ in range(stacks_n)]
for n in range(len(stack_building) - 2, -1, -1):
    for j in range(stacks_n):
        pos = 1 + j * 4
        if stack_building[n][pos] != ' ':
            stacks[j].append(stack_building[n][pos])

for line in lines[i+1:]:
    instruction = [int(s) for s in line.split(' ') if s != '' and s != 'move' and s != 'from' and s != 'to']
    to_move = stacks[instruction[1] - 1][-instruction[0]:]
    stacks[instruction[1] - 1] = stacks[instruction[1] - 1][:-instruction[0]]
    stacks[instruction[2] - 1].extend(to_move)

print(''.join([stack[-1] for stack in stacks]))