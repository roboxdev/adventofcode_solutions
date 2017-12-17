from aocframework import AoCFramework
from blist import blist


class Day(AoCFramework):
    test_cases = (
    )

    def go(self):
        pos = 0
        step = int(self.puzzle_input.strip())
        vortex = blist([0])
        for i in range(1, 50000001):
            pos = (pos + step) % len(vortex) + 1
            vortex.insert(pos, i)
            if i % 500000 == 0:
                print(i)
            pass
        return vortex[vortex.index(0)+1]


Day()
