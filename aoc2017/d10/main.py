from collections import deque

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('3,4,1,5', 12),
    )

    def go(self):
        puzzle_input = list(map(int, self.puzzle_input.split(',')))
        l = deque(list(range(5)) if self.test else list(range(256)))
        pos = 0
        skip_size = 0
        for length in puzzle_input:
            l.rotate(-pos)
            l = deque([*l][:length][::-1] + [*l][length:])
            l.rotate(pos)
            pos += length + skip_size
            skip_size += 1
        return l[0] * l[1]


Day()
