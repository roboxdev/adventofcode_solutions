from raw_input import raw_input

raw_input = raw_input
counter = 0

for index, obj in enumerate(raw_input):
    try:
        next = raw_input[index + 1]
    except IndexError:
        next = raw_input[0]
    print(obj, next)
    counter += int(obj) if next == obj else 0

print(counter)

