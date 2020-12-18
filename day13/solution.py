from operator import itemgetter

start = 0
buses = []

with open("./input.txt") as f:
    start, buses = f.read().strip().splitlines()

    start = int(start)
    buses = list(map(int, filter(lambda n: n != "x", buses.split(","))))


schedule = [ (bus, (int(start / bus) * bus) + bus) for bus in buses]
quickest = sorted(schedule, key=itemgetter(1))


print(start)
print(quickest)
print(quickest[0][0] * (quickest[0][1] - start))

start = 0
buses = []

with open("./input.txt") as f:
    start, buses = f.read().strip().splitlines()

    start = int(start)
    buses = [(i, int(v)) if v != "x" else (i, 0) for i,v in enumerate(buses.split(","))]

s = sorted(buses, key=itemgetter(1), reverse=True)
largest = s[0]
k = 0
c = 1
i = 0

while True:
    k += 1

    if k % 1000000 == 0:
        print(c * largest[1])


    if i == len(s):
        break

    if s[i][1] == 0:
        i += 1
        continue

    if i == 0:
        c += 1
        i += 1
        continue

    item = s[i]
    offset = largest[0] - item[0]
    t = largest[1] * c
    diff = t - offset
    mod = diff % item[1]

    if mod == 0:
        i += 1
    else:
        i = 0

print(c * largest[1] - largest[0])
