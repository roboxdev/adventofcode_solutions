import re

raw_puzzle_input = '''cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 17 c
cpy 18 d
inc a
dec d
jnz d -2
dec c
jnz c -5'''


test_puzzle_input = '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''


class Solver(object):
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input.splitlines()

    def cpy(self, x, y=None, state=None, run_at=None):
        state[y] = state[x] if x in 'abcd' else int(x)
        return run_at + 1

    def inc(self, x, y=None, state=None, run_at=None):
        state[x] += 1
        return run_at + 1

    def dec(self, x, y=None, state=None, run_at=None):
        state[x] -= 1
        return run_at + 1

    def jnz(self, x, y=None, state=None, run_at=None):
        if x in 'abcd':
            if state[x] != 0:
                return run_at + int(y)
        elif int(x):
                return run_at + int(y)
        return run_at + 1

    def go(self):
        registers = {
            'a': 0,
            'b': 0,
            'c': 1,
            'd': 0,
        }
        patterns = (
            (r'cpy (?P<x>.+) (?P<y>\w+)', self.cpy),
            (r'inc (?P<x>\w+)', self.inc),
            (r'dec (?P<x>\w+)', self.dec),
            (r'jnz (?P<x>.+) (?P<y>.+)', self.jnz),
        )
        run_command_at = 0
        while run_command_at < len(self.puzzle_input):
            command = self.puzzle_input[run_command_at]
            for pattern, function in patterns:
                match = re.match(pattern, command)
                if match:
                    run_command_at = function(**match.groupdict(),
                                              **{'state': registers, 'run_at': run_command_at})

        return registers['a']


if __name__ == '__main__':
    s = Solver(raw_puzzle_input)
    print(s.go())
    stest = Solver(test_puzzle_input)
    print(stest.go())