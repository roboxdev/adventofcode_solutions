from aocframework import AoCFramework
import numpy as np


class Day(AoCFramework):
    test_cases = (
        # (23, 2),
        # (1, 0),
        # (12, 3),
        # (1024, 31),
    )

    def go(self):
        start_at = (500, 500)
        m = np.zeros((1000, 1000), np.int)
        m[start_at[0], start_at[1]] = 1
        direction = 0
        directions = (
            (1, 0),  # down
            (0, 1),  # right
            (-1, 0),  # up
            (0, -1),  # left
        )
        current_coord = [*start_at]
        while True:
            side_x, side_y = list(map(sum, zip(current_coord, directions[(direction+1) % 4])))
            if m[side_x, side_y] == 0:
                direction += 1
            next_x, next_y = list(map(sum, zip(current_coord, directions[direction % 4])))
            value = np.sum(m[next_x-1:next_x+2, next_y-1:next_y+2]) - m[next_x, next_y]
            m[next_x, next_y] = value
            if value > int(self.puzzle_input):
                print(m[495:505, 495:505])
                return value
            current_coord = [next_x, next_y]


Day()
