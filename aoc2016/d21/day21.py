import re
from collections import deque

puzzle_input = '''rotate right 4 steps
swap letter b with letter e
swap position 1 with position 3
reverse positions 0 through 4
rotate left 5 steps
swap position 6 with position 5
move position 3 to position 2
move position 6 to position 5
reverse positions 1 through 4
rotate based on position of letter e
reverse positions 3 through 7
reverse positions 4 through 7
rotate left 1 step
reverse positions 2 through 6
swap position 7 with position 5
swap letter e with letter c
swap letter f with letter d
swap letter a with letter e
swap position 2 with position 7
swap position 1 with position 7
swap position 6 with position 3
swap letter g with letter h
reverse positions 2 through 5
rotate based on position of letter f
rotate left 1 step
rotate right 2 steps
reverse positions 2 through 7
reverse positions 5 through 6
rotate left 6 steps
move position 2 to position 6
rotate based on position of letter a
rotate based on position of letter a
swap letter f with letter a
rotate right 5 steps
reverse positions 0 through 4
swap letter d with letter c
swap position 4 with position 7
swap letter f with letter h
swap letter h with letter a
rotate left 0 steps
rotate based on position of letter e
swap position 5 with position 4
swap letter e with letter h
swap letter h with letter d
rotate right 2 steps
rotate right 3 steps
swap position 1 with position 7
swap letter b with letter e
swap letter b with letter e
rotate based on position of letter e
rotate based on position of letter h
swap letter a with letter h
move position 7 to position 2
rotate left 2 steps
move position 3 to position 2
swap position 4 with position 6
rotate right 7 steps
reverse positions 1 through 4
move position 7 to position 0
move position 2 to position 0
reverse positions 4 through 6
rotate left 3 steps
rotate left 7 steps
move position 2 to position 3
rotate left 6 steps
swap letter a with letter h
rotate based on position of letter f
swap letter f with letter c
swap position 3 with position 0
reverse positions 1 through 3
swap letter h with letter a
swap letter b with letter a
reverse positions 2 through 3
rotate left 5 steps
swap position 7 with position 5
rotate based on position of letter g
rotate based on position of letter h
rotate right 6 steps
swap letter a with letter e
swap letter b with letter g
move position 4 to position 6
move position 6 to position 5
rotate based on position of letter e
reverse positions 2 through 6
swap letter c with letter f
swap letter h with letter g
move position 7 to position 2
reverse positions 1 through 7
reverse positions 1 through 2
rotate right 0 steps
move position 5 to position 6
swap letter f with letter a
move position 3 to position 1
move position 2 to position 4
reverse positions 1 through 2
swap letter g with letter c
rotate based on position of letter f
rotate left 7 steps
rotate based on position of letter e
swap position 6 with position 1'''


test_puzzle_input = '''swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d'''


class Solver(object):
    def __init__(self, puzzle_input, start_string):
        self.puzzle_input = puzzle_input.splitlines()
        self.start_string = start_string

    def swap_position(self, x, y):
        x, y = int(x), int(y)
        l = list(self.start_string)
        l[x], l[y] = l[y], l[x]
        self.start_string = ''.join(l)

    def swap_letter(self, x, y):
        self.start_string = self.start_string.replace(x, '@').replace(y, x).replace('@', y)

    def rotate_n_steps(self, x, direction):
        x = int(x)
        d = 1 if direction == 'right' else -1
        deq = deque(self.start_string)
        deq.rotate(x*d)
        self.start_string = ''.join(deq)

    def revert_rotate_n_steps(self, x, direction):
        x = int(x)
        d = 1 if direction == 'left' else -1
        deq = deque(self.start_string)
        deq.rotate(x*d)
        self.start_string = ''.join(deq)

    @staticmethod
    def rotate_based_helper(s, x):
        i = s.index(x)
        add = 1 if i >= 4 else 0
        r = 1 + i + add
        deq = deque(s)
        deq.rotate(r)
        return ''.join(deq)

    def rotate_based(self, x):
        self.start_string = self.rotate_based_helper(self.start_string, x)

    def revert_rotate_based(self, x):
        for r in range(1, len(self.start_string)):
            deq = deque(self.start_string)
            deq.rotate(-r)
            s = ''.join(deq)
            s2 = self.rotate_based_helper(s, x)
            print(s, s2)
            if self.start_string == s2:
                self.start_string = s
                break

    def reverse_pos(self, x, y):
        x, y = int(x), int(y)
        s = self.start_string
        self.start_string = s[:x] + s[x:y+1][::-1] + s[y+1:]

    def move_pos(self, x, y):
        x, y = int(x), int(y)
        l = list(self.start_string)
        l.insert(y, l.pop(x))
        self.start_string = ''.join(l)

    def go(self):
        patterns = (
            (r'swap position (?P<x>.+) with position (?P<y>.+)', self.swap_position),
            (r'swap letter (?P<x>.+) with letter (?P<y>.+)', self.swap_letter),
            (r'rotate (?P<direction>left|right) (?P<x>.+) steps?', self.rotate_n_steps),
            (r'rotate based on position of letter (?P<x>.+)', self.rotate_based),
            (r'reverse positions (?P<x>.+) through (?P<y>.+)', self.reverse_pos),
            (r'move position (?P<x>.+) to position (?P<y>.+)', self.move_pos),
        )
        for operation in self.puzzle_input:
            for pattern, f in patterns:
                match = re.match(pattern, operation)
                if match:
                    f(**match.groupdict())
                    print(self.start_string)
        return self.start_string

    def go2(self):
        patterns = (
            (r'swap position (?P<x>.+) with position (?P<y>.+)', self.swap_position),
            (r'swap letter (?P<x>.+) with letter (?P<y>.+)', self.swap_letter),
            (r'rotate (?P<direction>left|right) (?P<x>.+) steps?', self.revert_rotate_n_steps),
            (r'rotate based on position of letter (?P<x>.+)', self.revert_rotate_based),
            (r'reverse positions (?P<x>.+) through (?P<y>.+)', self.reverse_pos),
            (r'move position (?P<y>.+) to position (?P<x>.+)', self.move_pos),
        )
        for operation in self.puzzle_input[::-1]:
            for pattern, f in patterns:
                match = re.match(pattern, operation)
                if match:
                    f(**match.groupdict())
                    print(self.start_string)
        return self.start_string


if __name__ == '__main__':
    test = Solver(test_puzzle_input, 'abcde')
    assert test.go() == 'decab'
    test_reverse = Solver('rotate based on position of letter d', 'decab')
    assert test_reverse.go2() == 'ecabd'
    test_reverse = Solver('rotate based on position of letter b', 'ecabd')
    assert test_reverse.go2() == 'abdec'
    test_reverse = Solver('move position 3 to position 0', 'abdec')
    assert test_reverse.go2() == 'bdeac'
    test_reverse = Solver('move position 1 to position 4', 'bdeac')
    assert test_reverse.go2() == 'bcdea'
    test_reverse = Solver('rotate left 1 step', 'bcdea')
    assert test_reverse.go2() == 'abcde'
    test_reverse = Solver('reverse positions 0 through 4', 'abcde')
    assert test_reverse.go2() == 'edcba'
    test_reverse = Solver('swap letter d with letter b', 'edcba')
    assert test_reverse.go2() == 'ebcda'
    test_reverse = Solver('swap position 4 with position 0', 'ebcda')
    assert test_reverse.go2() == 'abcde'
    test = Solver(test_puzzle_input, 'decab')
    assert test.go2() == 'abcde'

    s = Solver(puzzle_input, 'abcdefgh')
    print(s.go())
    uns = Solver(puzzle_input, 'fbgdceah')
    print(uns.go2())

