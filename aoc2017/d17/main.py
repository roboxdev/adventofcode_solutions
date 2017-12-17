from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''3''', 638),
    )

    def go(self):
        pos = 0
        step = int(self.puzzle_input.strip())
        vortex = [0]
        for i in range(1, 2018):
            pos = (pos + step) % len(vortex) + 1
            vortex.insert(pos, i)
            pass
        return vortex[pos + 1]


Day()
