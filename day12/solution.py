instructions = []

with open("./input.txt") as f:
    for line in f.read().strip().splitlines():
        instructions.append((line[0], int(line[1:])))


x = 0
y = 0
facing = 90

for instruction in instructions:
    action, value = instruction

    if action == "F":
        direction = (facing / 90) % 4
        if direction == 0:
            action = "N"
        if direction == 1:
            action = "E"
        if direction == 2:
            action = "S"
        if direction == 3:
            action = "W"

    if action == "N":
        y += value
    if action == "S":
        y -= value
    if action == "E":
        x += value
    if action == "W":
        x -= value
    if action == "L":
        facing -= value
    if action == "R":
        facing += value

    if facing < 0:
        facing = 360 + facing

print (abs(x) + abs(y), x, y)

wpx = 10
wpy = 1
shipx = 0
shipy = 0
facing = 90

for instruction in instructions:
    action, value = instruction


    if action == "F":
        shipx += wpx * value
        shipy += wpy * value

    if action == "N":
        wpy += value
    if action == "S":
        wpy -= value
    if action == "E":
        wpx += value
    if action == "W":
        wpx -= value

    if action == "R":
        while value > 0:
            tmp = wpx
            wpx = wpy
            wpy = -tmp
            value -= 90

    if action == "L":
        while value > 0:
            tmp = wpx
            wpx = -wpy
            wpy = tmp
            value -= 90

    print(instruction, (wpx, wpy), (shipx, shipy))

print(abs(shipx) + abs(shipy))
