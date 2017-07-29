from functools import reduce

# INIT, MULTIPLIER, DIVIDER = 20151125, 252533, 33554393
INIT, MULTIPLIER, DIVIDER = 20151125, 252553, 33554393


def manual_flat(index):
    return reduce(lambda x, y: x * MULTIPLIER % DIVIDER, range(index), INIT)


def manual_table(row, col):
    return sum(range(row + col - 1)) + col - 1


def table_pretty():
    table = []
    for row in range(1, 7):
        table.append([manual_flat(manual_table(row, col)) for col in range(1, 7)])
    return table

assert table_pretty()[-1][-1] == manual_flat(manual_table(6, 6))


# print(manual_table(2978, 3083))
# print(manual_flat(manual_table(2978, 3083)))

print(manual_table(8515, 7594))
print(manual_flat(manual_table(8515, 7594)))

#    | 1   2   3   4   5   6
# ---+---+---+---+---+---+---+
#  1 |  1   3   6  10  15  21
#  2 |  2   5   9  14  20
#  3 |  4   8  13  19
#  4 |  7  12  18
#  5 | 11  17
#  6 | 16

# 8515, 7594
# index 129733371
# value 13406114
# warn 8733226
