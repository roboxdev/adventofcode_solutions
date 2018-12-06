from operator import itemgetter
import numpy as np

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9''', 16),
    )

    @staticmethod
    def find_closest(coords, x, y):
        distances = []
        for coord_x, coord_y in coords:
            distances.append(abs(coord_x-x) + abs(coord_y - y))
        return sum(distances)

    def go(self):
        coords = [
            (int(x), int(y)) for x, y in map(
                lambda x: x.split(', '),
                self.linesplitted
            )
        ]
        min_x = min(coords, key=itemgetter(0))[0]
        max_x = max(coords, key=itemgetter(0))[0]
        min_y = min(coords, key=itemgetter(1))[1]
        max_y = max(coords, key=itemgetter(1))[1]
        field = np.full((max_x+1, max_y+1), -1, np.int)
        counter = 0
        for (x, y), value in np.ndenumerate(field):
            if value == -1:
                s = self.find_closest(coords, x, y)
                field[x, y] = s
                if s < (32 if self.test else 10000):
                    counter += 1
        print(field.T)
        return counter


Day()
