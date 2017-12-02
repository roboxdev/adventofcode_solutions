from raw_input import raw_input

raw_input = raw_input
counter = 0

for index, obj in enumerate(raw_input):
    l = len(raw_input)
    half = l / 2
    try:
        next = raw_input[int(index + half)]
    except IndexError:
        next = raw_input[int(index + half - l)]
    print(obj, next)
    counter += int(obj) if next == obj else 0

print(counter)

