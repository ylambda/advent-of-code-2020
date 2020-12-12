instructions = []

with open("./input.txt") as f:
    for line in f.read().strip().splitlines():
        instruction, arg = line.split(" ")
        arg = int(arg)
        instructions.append((instruction, arg))

visited = []
ip = 0
acc = 0
while True:

    if ip in visited:
        break

    visited.append(ip)

    instruction, arg = instructions[ip]

    if instruction == "nop":
        ip += 1
        continue
    if instruction == "acc":
        acc += arg
        ip += 1
        continue
    if instruction == "jmp":
        ip += arg
        continue

print(acc)


def execute(instructions):
    visited = []
    ip = 0
    acc = 0
    while True:
        if ip == len(instructions):
            return acc

        if ip in visited:
            return False

        visited.append(ip)

        instruction, arg = instructions[ip]

        if instruction == "nop":
            ip += 1
            continue
        if instruction == "acc":
            acc += arg
            ip += 1
            continue
        if instruction == "jmp":
            ip += arg
            continue
s=0
while True:
    modified = instructions[:]

    for i, instr in enumerate(modified[s:]):
        if instr[0] == "nop":
            s += i
            modified[s] = ("jmp", instr[1])
            break
        elif instr[0] == "jmp":
            s += i
            modified[s] = ("nop", instr[1])
            break

    print(modified[s], instructions[s])

    result = execute(modified)
    if result is not False:
        print(result)
        break
    else:
        print("{} / {}".format(s, len(instructions)))
    s += 1

    if s >= len(instructions):
        break
