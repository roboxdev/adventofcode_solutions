from itertools import product, combinations

raw_input = ''
with open('./raw_input.txt') as f:
    raw_input = f.read()


lines = raw_input.splitlines()

vals = [list(map(int, line.split())) for line in lines]

print(vals)


def find_result(line):
    c = combinations(line, 2)

    for a, b in c:
        minof, maxof = min([a, b]), max([a, b])
        if maxof % minof == 0:
            return maxof / minof

result = sum([find_result(line) for line in vals])
print(result)
