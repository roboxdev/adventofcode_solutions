from collections import deque
from functools import reduce

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''flqrgnkx''', 1242),
    )

    @staticmethod
    def knot_hash(s):
        puzzle_input = ','.join(map(str, s.strip().encode('ascii')))
        puzzle_input += ',' if puzzle_input else ''
        puzzle_input += '17,31,73,47,23'
        puzzle_input = list(map(int, puzzle_input.split(',')))
        l = deque(range(256))
        pos = 0
        skip_size = 0
        for _ in range(64):
            for length in puzzle_input:
                l.rotate(-pos)
                l = deque([*l][:length][::-1] + [*l][length:])
                l.rotate(pos)
                pos += length + skip_size
                skip_size += 1
        sparse_hash = list(zip(*[iter(l)] * 16))
        dense_hash = [reduce(lambda a, b: a ^ b, v) for v in sparse_hash]
        return ''.join(map(lambda v: format(v, '02x'), dense_hash))

    def get_field(self):
        field = []
        for i in range(128):
            r = '{}-{}'.format(self.puzzle_input.strip(), i)
            hashed = self.knot_hash(r)
            bined = bin(int(hashed, base=16))
            field.append([1 if v == '1' else 0 for v in bined[2:].rjust(128, '0')])
        return field

    @staticmethod
    def get_region(field, init_x, init_y):
        region = []
        to_process = [(init_x, init_y)]
        while to_process:
            t, to_process = to_process[:], []
            region += t
            for x, y in t:
                top = (x, y-1) if y != 0 and field[y-1][x] else ()
                bot = (x, y+1) if y != 127 and field[y+1][x] else ()
                left = (x-1, y) if x != 0 and field[y][x-1] else ()
                right = (x+1, y) if x != 127 and field[y][x+1] else ()
                to_process += list(
                    filter(
                        lambda v: v not in region and v not in to_process,
                        filter(bool, (top, bot, left, right))
                    )
                )
                pass
        return region

    def go(self):
        field = self.get_field()
        mark = 0
        while True:
            flatten = sum(field, [])
            try:
                i = flatten.index(1)
            except ValueError:
                return mark
            x, y = i % 128, i // 128
            to_null = self.get_region(field, x, y)
            for x, y in to_null:
                field[y][x] = 0
            mark += 1


Day()
