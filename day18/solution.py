lines = []
with open("./test.txt") as f:
    lines = f.read().strip().splitlines()

def evaluate(s):
    tokens = s.split(" ");
    i = 0;
    t = 0
    operator = None

    assert(tokens[0] == "(")
    assert(tokens[-1] == ")")
    tokens.pop(0)
    tokens.pop()

    while i != len(tokens):
        token = tokens[i]
        t2 = 0

        if token == "+" or token == "*":
            i += 1
            operator = token
            continue

        if token == "(":
            depth = 0
            j = 0

            for token2 in tokens[i:]:
                j += 1
                if token2 == "(":
                    depth += 1
                if token2 == ")":
                    depth -= 1
                if depth == 0:
                    break

            t2 = evaluate(" ".join(tokens[i:i+j]))
            i = i + j

        elif token in "0123456789":
            i += 1
            t2 = int(token)

        if operator != None:
            if operator == "+":
                t += t2
            if operator == "*":
                t *= t2
        else:
            t = t2

    return t


ss = 0
for line in lines:
    line = "(" + line + ")"
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    ss += evaluate(line)

print(ss)

def evaluate2(s):
    tokens = s.split(" ");
    tokens.pop(0)
    tokens.pop()

    tree = []
    operator = None
    args = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token == "(":
            idx = find_closing(tokens[i:])
            args.append(evaluate2(" ".join(tokens[i:i+idx])))
            i += idx

        i += 1
        if token in "0123456789":
            args.append(int(token))

        if token in "+*":
            operator = token



def find_closing(tokens):
    depth = 0
    j = 0

    for token in tokens:
        j += 1
        if token == "(":
            depth += 1
        if token == ")":
            depth -= 1
        if depth == 0:
            break

    return j

ss = 0
for line in lines:
    line = "(" + line + ")"
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    ss += evaluate2(line)
