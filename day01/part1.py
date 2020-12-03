import itertools

lines = []

with open("./input.txt") as f:
    for line in f:
        lines.append(int(line.strip()))


combos = list(itertools.combinations(lines, 3))

for combo in combos:
    ssum = combo[0] + combo[1] + combo[2]
    if ssum == 2020:
        print(combo[0] * combo[1] * combo[2])
        break
