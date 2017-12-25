from collections import deque

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
    )

    def go(self):
        steps = 12459852
        state = 'a'
        states = {
            'a': (
                (1, 1, 'b'),
                (1, -1, 'e'),
            ),
            'b': (
                (1, 1, 'c'),
                (1, 1, 'f'),
            ),
            'c': (
                (1, -1, 'd'),
                (0, 1, 'b'),
            ),
            'd': (
                (1, 1, 'e'),
                (0, -1, 'c'),
            ),
            'e': (
                (1, -1, 'a'),
                (0, 1, 'd'),
            ),
            'f': (
                (1, 1, 'a'),
                (1, 1, 'c'),
            ),
        }
        tape = deque([0] * steps)
        for _ in range(steps):
            to_write, shift, next_state = states[state][tape[0]]
            tape[0] = to_write
            tape.rotate(shift)
            state = next_state
        return tape.count(1)


Day()
