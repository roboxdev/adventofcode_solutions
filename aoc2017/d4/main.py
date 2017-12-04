raw_input = ''
with open('./raw_input.txt') as f:
    raw_input = f.read()


lines = raw_input.splitlines()

counter = 0
for line in lines:
    splitted = line.split()
    if len(splitted) == len(set(splitted)):
        counter += 1

print(counter)