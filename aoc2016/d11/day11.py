import timeit
from functools import reduce
from itertools import combinations

raw_puzzle_input = '''The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant.'''


# elements = (
#     ('promethium', 1),
#     ('cobalt', 2),
#     ('curium', 3),
#     ('ruthenium', 4),
#     ('plutonium', 5),
# )

elems = {-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7}
possible_floor = []

for combination_len in range(0, len(elems) + 1):
    for subset in combinations(elems, combination_len):
        if not list(filter(lambda x: abs(x) not in subset and max(subset) > 0, subset)):
            possible_floor.append(set(subset))


class Facility(tuple):
    def find_possible_moves(self):
        possible_moves = []
        elevator_position = self[4]
        moves_map = {
            0: ((1, self[1]), ),
            1: ((2, self[2]), (0, self[0])),
            2: ((3, self[3]), (1, self[1])),
            3: ((2, self[2]), ),
        }
        current_floor = self[elevator_position]
        for side_floor_index, side_floor in moves_map[elevator_position]:
            elevate_combinations = list(combinations(current_floor, 2)) + list(combinations(current_floor, 1))
            filtered_elevate_combinations = filter(
                lambda x: not (len(x) == 2 and min(x) < 0 < max(x) and abs(min(x)) != max(x)),
                elevate_combinations)
            for to_elevate in filtered_elevate_combinations:
                to_elevate = set(to_elevate)
                with_elevator_arrived = side_floor | to_elevate
                with_elevator_dispatched = current_floor - to_elevate
                if with_elevator_arrived in possible_floor \
                        and with_elevator_dispatched in possible_floor:
                    new_facility_tuple = [set(i) if isinstance(i, set) or isinstance(i, frozenset) else i for i in self]
                    new_facility_tuple[elevator_position].difference_update(to_elevate)
                    new_facility_tuple[side_floor_index].update(to_elevate)
                    new_facility_tuple[4] = side_floor_index
                    frozen_tuple = tuple(frozenset(i) if isinstance(i, set) else i for i in new_facility_tuple)
                    possible_moves.append(Facility(frozen_tuple))
        return possible_moves


class Solver(object):
    def __init__(self, start, finish):
        super(Solver, self).__init__()
        self.start = Facility(start)
        self.finish = Facility(finish)
        self.start = Facility(finish)
        self.finish = Facility(start)

    def go(self):
        start = timeit.default_timer()
        d = 0
        field = set()
        new_moves = [self.start]
        while True:
            wave_start = timeit.default_timer()
            temp = set()
            for f in new_moves:
                for move in f.find_possible_moves():
                    if move and move not in field:
                        temp.add(move)
                        if move == self.finish:
                            print('SOLUTION:', d+1)
                            raise
            new_moves = temp
            field |= temp
            d += 1
            print(len(new_moves), d, timeit.default_timer() - start, timeit.default_timer() - wave_start)

    # def go(self):
    #     start = timeit.default_timer()
    #     field = []
    #     d = 0
    #     new_moves = [self.start]
    #     while True:
    #         wave_start = timeit.default_timer()
    #         temp = []
    #         for f in new_moves:
    #             for move in f.find_possible_moves():
    #                 if move and move not in temp:
    #                     if move == self.finish:
    #                         print('SOLUTION:', d + 1)
    #                         raise
    #                     temp.append(move)
    #         field += new_moves
    #         new_moves = temp
    #         print(len(new_moves), d, len(field), timeit.default_timer() - start,
    #               timeit.default_timer() - wave_start)
    #         d += 1


def get_finish(start):
    finish = (
        frozenset(),
        frozenset(),
        frozenset(),
        frozenset(reduce(lambda x, y: x | y, start[:-1])),
        3,
    )
    return finish


if __name__ == '__main__':
    test_start = (
        frozenset({-1, -2}),
        frozenset({1}),
        frozenset({2}),
        frozenset(),
        0,
    )
    test = Solver(test_start, get_finish(test_start))
    s_start = (
        frozenset({-1, 1}),
        frozenset({2, 3, 4, 5}),
        frozenset({-2, -3, -4, -5}),
        frozenset(),
        0,
    )
    s_start = (
        frozenset({-1, 1, 6, -6, 7, -7}),
        frozenset({2, 3, 4, 5}),
        frozenset({-2, -3, -4, -5}),
        frozenset(),
        0,
    )
    s = Solver(s_start, get_finish(s_start))
    # test.go()
    s.go()
