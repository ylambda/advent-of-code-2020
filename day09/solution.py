numbers = []
with open("./input.txt") as f:
    numbers = [ int(n) for n in f.read().strip().splitlines() ]

preamble = 25
i = 0


def validate(numbers, preamble, i):
    idx = preamble + i
    target = numbers[idx]
    snumbers = numbers[idx-preamble:idx].copy()

    snumbers.sort()
    largest = snumbers[-1] + snumbers[-2]
    smallest = snumbers[0] + snumbers[1]

    if largest < target:
        return False

    if smallest > target:
        return False

    return True

while validate(numbers, preamble, i):
    i += 1

p1 = numbers[preamble+i]
print(p1)

def p2():
    j = 0
    while True:
        k = len(numbers) - j
        while k >= j:
            total = sum(numbers[j:k])
            if total == p1 and len(numbers[j:k]) >= 2:
                snumbers = numbers[j:k].copy()
                snumbers.sort()

                print(snumbers[0], snumbers[-1], snumbers[0] + snumbers[-1])
                return
            else:
                k -= 1
        j += 1

p2()


