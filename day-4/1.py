with open("input.txt", "r") as f:
    lines = [[[int(n) for n in elf.split("-")] for elf in line.strip().split(",")] for line in f.readlines()]

total = 0
for line in lines:
    elf1 = line[0]
    elf2 = line[1]
    for i in range(elf1[0], elf1[1] + 1):
        if i in range(elf2[0], elf2[1] + 1):
            total += 1
            break

print(total)