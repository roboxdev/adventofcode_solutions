from blist import blist


class Solver(object):
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def go(self):
        elves = {*range(1, self.puzzle_input+1)}
        exclude_even = True
        while True:
            to_exclude = set(sorted(elves)[int(exclude_even)::2])
            exclude_even = True if sorted(to_exclude)[-1] == sorted(elves)[-1] else False
            elves -= to_exclude
            if len(elves) == 1:
                break
        return list(elves)[0]

    def go2(self):
        # elves = {*range(1, self.puzzle_input+1)}
        sorted_elves = blist([*range(1, self.puzzle_input+1)])
        current_stealer = 1
        while len(sorted_elves) > 1:
            if current_stealer > sorted_elves[-1]:
                current_stealer = 1
                continue
            if current_stealer not in sorted_elves:
                current_stealer += 1
                continue
            current_stealer_index = sorted_elves.index(current_stealer)
            elf_across_index = (int(len(sorted_elves) / 2) + current_stealer_index)
            # if len(sorted_elves) <= 3:
            #     raise
            # try:
            #     to_exclude = {sorted_elves[elf_across_index]}
            # except IndexError:
            #     to_exclude = {sorted_elves[elf_across_index - len(sorted_elves)]}
            # elves -= to_exclude
            try:
                sorted_elves.pop(elf_across_index)
            except IndexError:
                sorted_elves.pop(elf_across_index - len(sorted_elves))
            current_stealer += 1
            if len(sorted_elves) % 1000 == 0:
                print(len(sorted_elves))

        return list(sorted_elves)[0]


if __name__ == '__main__':
    test = Solver(5)
    # assert test.go() == 3
    assert test.go2() == 2
    # test = Solver(6)
    # assert test.go() == 5
    # test = Solver(7)
    # assert test.go() == 7
    test = Solver(8)
    assert test.go2() == 7
    # assert test.go() == 1
    s = Solver(3014387)
    # print(s.go())
    print(s.go2())
