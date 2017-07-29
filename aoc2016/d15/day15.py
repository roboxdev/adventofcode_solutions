"""
Disc #1 has 17 positions; at time=0, it is at position 5.
Disc #2 has 19 positions; at time=0, it is at position 8.
Disc #3 has 7 positions; at time=0, it is at position 1.
Disc #4 has 13 positions; at time=0, it is at position 7.
Disc #5 has 5 positions; at time=0, it is at position 1.
Disc #6 has 3 positions; at time=0, it is at position 0.
"""


class Solver(object):
    def __init__(self, disks):
        self.disks = disks

    def get_combo(self, t):
        combo = [(t + init_pos + i + 1) % total_pos for i, (init_pos, total_pos) in enumerate(self.disks)]
        return combo

    def go(self):
        t = 0
        while True:
            if not any(self.get_combo(t)):
                return t
            t += 1

if __name__ == '__main__':
    test_disks = (
        (4, 5),
        (1, 2),
    )
    test = Solver(test_disks)
    print(test.go())

    puzzle_input = (
        (5, 17),
        (8, 19),
        (1, 7),
        (7, 13),
        (1, 5),
        (0, 3),
    )
    s = Solver(puzzle_input)
    print(s.go())

    puzzle_input = (
        (5, 17),
        (8, 19),
        (1, 7),
        (7, 13),
        (1, 5),
        (0, 3),
        (0, 11),  # Part 2
    )
    s = Solver(puzzle_input)
    print(s.go())
