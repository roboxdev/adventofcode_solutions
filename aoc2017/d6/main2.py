from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('0 2 7 0', 4),
    )

    @property
    def puzzle_input(self):
        return tuple(map(int, self.raw_puzzle_input.split()))

    def go(self):
        print(self.puzzle_input)
        log = [self.puzzle_input]
        while True:
            last_state = log[-1]
            bank_index = last_state.index(max(last_state))
            bank_value = last_state[bank_index]
            new_state = [*last_state]
            new_state[bank_index] = 0
            for i in range(bank_index+1, bank_index + 1 + bank_value):
                new_state[i % len(self.puzzle_input)] += 1

            if new_state in log:
                return len(log) - log.index(new_state)
            else:
                log.append(new_state)


Day()
