raw_input = ''
with open('./raw_input.txt') as f:
    raw_input = f.read()


lines = raw_input.splitlines()

vals = [list(map(int, line.split())) for line in lines]

print(vals)

checksum = 0
for line in vals:
    checksum += max(line) - min(line)

print(checksum)