from collections import deque
from functools import reduce

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''flqrgnkx''', 8108),
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

    def go(self):
        answer = 0
        for i in range(128):
            r = '{}-{}'.format(self.puzzle_input.strip(), i)
            hashed = self.knot_hash(r)
            bined = bin(int(hashed, base=16))
            t = bined[2:].replace('1', '#').replace('0', '.')
            answer += t.count('#')
        return answer


Day()
