from collections import Counter
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
8, 9''', 17),
    )

    @staticmethod
    def find_closest(coords, x, y):
        distances = []
        for coord_x, coord_y in coords:
            distances.append(abs(coord_x-x) + abs(coord_y - y))
        closest = min(enumerate(distances), key=itemgetter(1))
        return closest[0] if distances.count(closest[1]) == 1 else -2

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
        for i, (x, y) in enumerate(coords):
            field[x, y] = i
        for (x, y), value in np.ndenumerate(field):
            if value == -1:
                field[x, y] = self.find_closest(coords, x, y)
        print(field.T)
        candidates = Counter(field.flatten()).most_common()
        print(coords)
        to_exclude = set(field[0])
        to_exclude = to_exclude.union(set(field[max_x]))
        to_exclude = to_exclude.union(set(field[:, 0]))
        to_exclude = to_exclude.union(set(field[:, max_y]))
        for i, count in candidates:
            if i not in to_exclude:
                return count


Day()
