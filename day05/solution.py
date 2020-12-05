import math

bpasses = []
with open("./input.txt") as f:
    bpasses = f.read().strip().splitlines()

def partition(letter, partition):
    lower, upper = partition
    size = upper - lower
    half = size / 2

    if letter == "F" or letter == "L":
        return (lower, lower + math.floor(half))

    if letter == "B" or letter == "R":
        return (lower + math.ceil(half), upper)

def decode_row(bpass):
    r = (0, 127)
    for c in bpass[:7]:
        r = partition(c, r)
    return r[0]

def decode_col(bpass):
    r = (0, 8)
    for c in bpass[7:]:
        r = partition(c, r)
    return r[0]

def decode_bpass(bpass):
    row = decode_row(bpass)
    col = decode_col(bpass)

    return (row * 8) + col

seats = sorted([decode_bpass(bpass) for bpass in bpasses])
highest = max(seats)
print(highest)

prev = seats[0]
for seat in seats[1:]:
    if prev+2 == seat:
        print(seat-1)
    else:
        prev = seat
