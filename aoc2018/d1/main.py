from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
    )

    def go(self):
        frequency = 0
        for op in self.linesplitted:
            frequency += int(op)

        return frequency

Day()
