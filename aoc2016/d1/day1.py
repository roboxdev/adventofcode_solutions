raw_puzzle_input = 'R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5,' \
               ' L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1,' \
               ' R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3,' \
               ' R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2,' \
               ' R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2,' \
               ' R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5,' \
               ' L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5'

# puzzle_input = 'R2, R2, R2, R2, R2, R2, R2, R2, R2, R2, R2, R2, R2, R2, L2, L2, L2, L2, L2, L2, L2, L2, L2, L2'


class Walker(object):
    position_x = 0
    position_y = 0
    heading = 0
    raw_puzzle_input = ''
    visited = []

    @property
    def coords(self):
        return self.position_x, self.position_y

    @property
    def direction_mapping(self):
        return {
            0: self.go_north,  # ↑
            1: self.go_east,  # →
            2: self.go_south,  # ↓
            3: self.go_west,  # ←
        }

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input.split(', ')
        super(Walker, self).__init__()

    def go_north(self, distance):
        self.position_y += distance

    def go_east(self, distance):
        self.position_x += distance

    def go_south(self, distance):
        self.position_y -= distance

    def go_west(self, distance):
        self.position_x -= distance

    def go(self):
        for step in self.puzzle_input:
            turn = step[0]
            distance = int(step[1:])
            if turn == 'R':
                self.heading += 1
            else:
                self.heading -= 1
            self.direction_mapping[self.heading % 4](distance)
            print(step, self.coords)
        return abs(self.position_x) + abs(self.position_y)

    def go2(self):
        for step in self.puzzle_input:
            turn = step[0]
            distance = int(step[1:])
            if turn == 'R':
                self.heading += 1
            else:
                self.heading -= 1
            for _ in range(distance):
                print(step, self.coords)
                self.direction_mapping[self.heading % 4](1)
                if self.coords in self.visited:
                    return step, self.coords, abs(self.position_x) + abs(self.position_y)
                else:
                    self.visited += self.coords,


if __name__ == '__main__':
    w = Walker(raw_puzzle_input)
    print(w.go())
    w = Walker(raw_puzzle_input)
    print(w.go2())
