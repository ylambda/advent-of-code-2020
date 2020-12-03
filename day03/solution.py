with open("./input.txt") as f:
    grid = [line for line in f.read().strip().splitlines()]


width = len(grid[0])
height = len(grid)

def slope(grid, incr_x, incr_y):
    x=0
    y=0

    count = 0

    while y < height:
        if grid[y][x] == "#":
            count += 1

        x = (x + incr_x) % width
        y += incr_y

    return count

print("part 1: {}".format(slope(grid, 3, 1)))

p2 = []
p2.append(slope(grid, 1, 1))
p2.append(slope(grid, 3, 1))
p2.append(slope(grid, 5, 1))
p2.append(slope(grid, 7, 1))
p2.append(slope(grid, 1, 2))

import math 

print("part 2: {}".format(math.prod(p2)))
