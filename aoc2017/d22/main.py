import numpy as np

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''..#
#..
...''', 5587),
)

    directions = (
        complex(-1, 0),
        complex(0, 1),
        complex(1, 0),
        complex(0, -1),
    )

    @staticmethod
    def left(d):
        return (d - 1) if d != 0 else 3

    @staticmethod
    def right(d):
        return (d + 1) if d != 3 else 0

    def go(self):
        d = 0
        l = len(self.linesplitted) // 2 + 1
        middle_i = 500
        field_pad = middle_i - l + 1
        start = np.array(list(map(list, self.linesplitted)))
        field = np.pad(start, ((field_pad, field_pad), (field_pad, field_pad)), mode='constant', constant_values=0)
        pos = complex(middle_i, middle_i)
        infections = 0
        for burst in range(10000):
            if self.test and burst == 7:
                assert infections == 5
            if self.test and burst == 70:
                assert infections == 41
            cur_node_infected = field[int(pos.real), int(pos.imag)] == '#'
            d = self.right(d) if cur_node_infected else self.left(d)
            field[int(pos.real), int(pos.imag)] = '.' if cur_node_infected else '#'
            infections += not cur_node_infected
            pos = pos + self.directions[d]
        return infections


Day()
