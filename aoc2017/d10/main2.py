from collections import deque

from aocframework import AoCFramework
from functools import reduce


class Day(AoCFramework):
    test_cases = (
        ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
        ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e'),
        ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
        ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
    )

    def go(self):
        puzzle_input = ','.join(map(str, self.puzzle_input.encode('ascii')))
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
        sparse_hash = zip(*[iter(l)]*16)
        dense_hash = [reduce(lambda a, b: a ^ b, v) for v in sparse_hash]
        answer = ''.join(map(lambda v: format(v, '02x'), dense_hash))
        return answer


Day()
