from aocframework import AoCFramework
import numpy as np
import re


class Day(AoCFramework):
    test_cases = (
        ('''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2''', 4
         ),)

    def parse(self, s):
        pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
        match = re.match(pattern, s)
        return tuple(map(int, match.groups()))

    @staticmethod
    def asdf(a, axis):
        print(a, axis)

    def go(self):
        field = np.zeros((1500, 1500), np.int)
        # field = np.zeros((10, 10), np.int)
        parsed = [self.parse(s) for s in self.linesplitted]
        assert len(parsed) == len(self.linesplitted)
        for id_, x, y, width, height in parsed:
            a = field[x:x + width, y:y + height]
            a[a != 0] = -1
            a[a == 0] = id_
        pass
        unique, counts = np.unique(field, return_counts=True)
        return dict(zip(unique, counts))[-1]

Day()
