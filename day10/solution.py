adapters = []

with open("./input.txt") as f:
    adapters = [ int(i) for i in f.read().strip().splitlines()]

adapters.sort()

jolts = 0
d1 = 0
d3 = 1
prev = 0
for i, a in enumerate(adapters):
    diff = abs(prev - a)
    jolts += a
    prev = a
    if diff > 3:
        print('diff too high')
        break
    if diff == 1:
        d1 += 1
    elif diff == 3:
        d3 += 1

print(d1 * d3)

adapters.insert(0, 0)

c = {}
def connect(a):
    print(a)
    limit = min(len(a) - 1, 3)
    t = 0

    print("lim", limit)
    if limit == 0:
        t += 1
    else:
        for i in range(0, limit):
            j = i + 1
            if a[j] - a[0] > 3:
                continue
            else:
                if a[j] not in c:
                    connect(a[j:])
                t += c[a[j]]

    c[a[0]] = t
    return t

print(connect(adapters))
