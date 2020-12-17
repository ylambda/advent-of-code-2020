import math

width = 0
height = 0
seats = []

with open("./input.txt") as f:
    inp = f.read().strip()
    width = inp.index("\n")
    lines = inp.splitlines()
    seats = [seat for seat in "".join(lines)]
    height = int((len(seats) / width))

def process(plan):
    newplan = plan.copy()
    for i, c in enumerate(plan):
        if c == ".":
            continue
        occupied, empty = counts(plan, i)
        if c == "#" and occupied >= 4:
            newplan[i] = "L"
        elif c == "L" and occupied == 0:
            newplan[i] = "#"

    return newplan

def counts(plan, i):
    nw = space(plan, i, -1, -1)
    n = space(plan, i, 0, -1)
    ne = space(plan, i, 1, -1)
    e = space(plan, i, 1, 0)
    se = space(plan, i, 1, 1)
    s = space(plan, i, 0, 1)
    sw = space(plan, i, -1, 1)
    w = space(plan, i, -1, 0)
    me = space(plan, i, 0, 0)

    grid = [nw, n, ne, w, e, sw, s, se]
    empty = 0
    occupied = 0

    for i in grid:
        if i == "#":
            occupied += 1
        if i == "L":
            empty += 1


    return occupied, empty


def space(plan, i, x, y):
    origin_x = i % width
    origin_y = math.floor(i / width)
    new_x = x + origin_x
    new_y = y + origin_y
    pos = (i + (y * width) + x)

    if new_x < 0 or new_x > (width-1) or new_y < 0 or new_y > (height-1):
        return "."
    else:
        return plan[pos]

prev = seats.copy()
def print_seats(seats):
    lines = []
    line = ""
    for i, s in enumerate(seats):
        line = line + s
        if (1 + i) % width == 0:
            lines.append(line)
            line = ""
    print("\n".join(lines))
    print("")

rounds = 0
while True:
    newplan = process(prev)
    rounds += 1
    if "".join(newplan) == "".join(prev):
        print_seats(newplan)
        c = 0
        for i in newplan:
            if i == "#":
                c += 1
        print(c)
        break

    else:
        prev = newplan
