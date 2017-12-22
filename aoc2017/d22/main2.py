import numpy as np

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''..#
#..
...''', 2511944),
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
        for burst in range(10000000):
            if burst % 100000 == 0:
                print(f'{burst // 100000}%')
            if self.test and burst == 100:
                assert infections == 26

            cur_node_status = field[int(pos.real), int(pos.imag)]
            movement_map = {
                '': self.left,
                '.': self.left,
                'W': lambda v: v,
                '#': self.right,
                'F': lambda v: self.left(self.left(v))
            }
            d = movement_map[cur_node_status](d)
            status_map = {
                '': 'W',
                '.': 'W',
                'W': '#',
                '#': 'F',
                'F': '.',
            }
            field[int(pos.real), int(pos.imag)] = status_map[cur_node_status]
            infections += cur_node_status == 'W'
            pos = pos + self.directions[d]
        return infections


Day()
