db = []

with open("./input.txt") as f:
    for line in f.read().strip().splitlines():
        rules, password = line.split(":")
        password = password.strip()
        rules, letter = rules.split(" ")
        minimum = int(rules.split("-")[0])
        maximum = int(rules.split("-")[1])

        db.append([password, letter, minimum, maximum])

def validate(entry):
    count = 0

    for i in entry[0]:
        if i == entry[1]:
            count += 1

    return count >= entry[2] and count <= entry[3]

valid = 0
for entry in db:
    if validate(entry):
        valid += 1
print("part 1: {}".format(valid))

def validate_2(entry):
    count = 0

    if entry[0][entry[2]-1] == entry[1]:
        count += 1

    if entry[0][entry[3]-1] == entry[1]:
        count += 1


    return count == 1

valid_2 = 0
for entry in db:
    if validate_2(entry):
        valid_2 += 1
print("part 2: {}".format(valid_2))
