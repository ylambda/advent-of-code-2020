groups = []
with open("./input.txt") as f:
    groups = f.read().strip().split("\n\n")

group_total = 0
total = 0

for group in groups:
    answers = {}
    for answer in group.split("\n"):
        for c in answer:
            answers[c] =  1 + answers.get(c, 0)
            total += 1

    group_total += len(answers.keys())

print(group_total)

agree = 0
for group in groups:
    answers = {}
    people = group.split("\n")
    
    for answer in people:
        for c in answer:
            answers[c] =  1 + answers.get(c, 0)
            total += 1

    for k,v in answers.items():
        if v == len(people):
            agree += 1

print(agree)

