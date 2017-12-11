from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('ne,ne,ne', 3),
        ('ne,ne,sw,sw', 0),
        ('ne,ne,s,s', 2),
        ('se,sw,se,sw,sw', 3),
        ('n,n,ne,ne', 4),
        ('ne,ne,ne,se', 4),
        ('nw,nw,s', 2),
        ('nw,nw,sw', 3),
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
        for d in self.puzzle_input.strip().split(','):
            coord += directions_map[d]
        x, y = int(coord.real), int(coord.imag)
        abs_x, abs_y = abs(x), abs(y)
        answer = max(abs_x, abs_y) if abs_x + abs_y == abs(x + y) else abs(x - y)
        return answer


Day()
