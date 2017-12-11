from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
    )

    def go(self):
        directions_map = {
            'nw': complex(-1, 0),
            'n': complex(-1, -1),
            'ne': complex(0, -1),
            'sw': complex(0, 1),
            's': complex(1, 1),
            'se': complex(1, 0),
        }

        coord = complex(0, 0)
        furthest = 0
        for d in self.puzzle_input.strip().split(','):
            coord += directions_map[d]
            x, y = int(coord.real), int(coord.imag)
            abs_x, abs_y = abs(x), abs(y)
            furthest = max(furthest, max(abs_x, abs_y) if abs_x + abs_y == abs(x + y) else abs(x - y))
        return furthest


Day()
