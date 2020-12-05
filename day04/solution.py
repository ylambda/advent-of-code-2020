import re
passports = []

with open("./input.txt") as f:
    passport = ""
    for line in f.read().strip().splitlines():
        if line == "":
            passports.append(passport.strip())
            passport = ""
        else:
            passport += line + " "

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

part_1 = 0
for passport in passports:
    valid = True

    for field in fields:
        if (field+":") not in passport and field != "cid":
            valid = False
            break

    if valid:
        part_1 += 1

print("part 1: {}".format(part_1))

part_2 = 0
for passport in passports:
    valid = True
    items = passport.split(" ")

    for field in fields:
        if (field+":") not in passport and field != "cid":
            valid = False
            break

    if not valid:
        continue

    for item in items:
        key, value = item.split(":")
        value = value.strip()

        if key == "byr":
            value = int(value)
            if value < 1920 or value > 2002:
                valid = False
                break
            continue

        if key == "iyr":
            value = int(value)
            if value < 2010 or value > 2020:
                valid = False
                break
            continue

        if key == "eyr":
            value = int(value)
            if value < 2020 or value > 2030:
                valid = False
                break
            continue

        if key == "hgt":
            if "cm" in value:
                value = int(value.split("cm")[0])
                if value < 150 or value > 193:
                    valid = False
                    break
            elif "in" in value:
                value = int(value.split("in")[0])
                if value < 59 or value > 76:
                    valid = False
                    break
            else:
                valid = False
                break
            continue

        if key == "hcl":
            r = re.compile('^#[0-9a-f]{6}$')
            if not r.match(value):
                valid = False
                break
            continue

        if key == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
                break
            continue

        if key == "pid":
            if not value.isnumeric() or not len(value) == 9:
                valid = False
                break
            continue

    if valid:
        part_2 += 1

print("part 2: {}".format(part_2))
