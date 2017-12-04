raw_input = ''
with open('./raw_input.txt') as f:
    raw_input = f.read()


lines = raw_input.splitlines()

counter = 0
for line in lines:
    p = [''.join(sorted(v)) for v in line.split()]
    if len(p) == len(set(p)):
        counter += 1

print(counter)
