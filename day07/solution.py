
rules = {}

with open("./input.txt") as f:
    for line in f.read().strip().splitlines():
        subject, out = line.split("bags contain")
        bag_output = []
        if out.strip().startswith("no"):
            rules[subject.strip()] = []
            continue
        for bag in out.strip().split(", "):
            words = bag.split(" ")
            count = int(words[0])
            name = " ".join(words[1:3]).strip()
            bag_output.append((count, name))
        rules[subject.strip()] =  bag_output

def find_holder(target):
    holders = []
    for rule, values in rules.items():
        for v in values:
            if v[1] == target:
                holders.append(rule)
    return holders

search = ["shiny gold"]
results = set()

while len(search):
    item = search.pop()
    holders = find_holder(item)
    for holder in holders:
        if holder not in results:
            search.append(holder)
    results.update(holders)
print(len(results))

sizes = {}

def calculate_bags(key):
    count = 0

    for c, name in rules[key]:
        if name in sizes:
            count += c + (c * sizes[name])
        elif len(rules[name]) == 0:
            count += c * 1
        else:
            count += c + (c * calculate_bags(name))

    if not key in sizes:
        sizes[key] = count

    print(key, count, rules[key])

    return count

print(calculate_bags("shiny gold"))
