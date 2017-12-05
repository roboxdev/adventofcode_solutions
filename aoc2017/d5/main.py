from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''0
        3
        0
        1
        -3''', 5),
    )

    def go(self):
        self.linesplitted = list(map(int, self.linesplitted))
        steps_counter = 0
        current_pos = 0
        while True:
            if current_pos < 0:
                return steps_counter
            try:
                t = current_pos
                next_pos = self.linesplitted[current_pos] + current_pos
                current_pos = next_pos
                self.linesplitted[t] += 1
            except IndexError:
                return steps_counter
            steps_counter += 1

Day()
