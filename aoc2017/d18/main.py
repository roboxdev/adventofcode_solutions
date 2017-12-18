import re
from collections import deque, defaultdict

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2''', 4),
    )

    def snd(self, x):
        self.last_sound = self.d[x]

    def set(self, x, y):
        self.d[x] = self.d[y] if y.isalpha() else int(y)

    def add(self, x, y):
        self.d[x] += self.d[y] if y.isalpha() else int(y)

    def mul(self, x, y):
        self.d[x] *= self.d[y] if y.isalpha() else int(y)

    def mod(self, x, y):
        self.d[x] %= self.d[y] if y.isalpha() else int(y)

    def rcv(self, x):
        assert self.d[x] == 0

    def jgz(self, x, y):
        if self.d[x] > 0:
            self.operation_pos += int(y) - 1

    def go(self):
        self.last_sound = 0
        self.d = defaultdict(int)
        self.operation_pos = 0
        patterns = (
            (r'snd (?P<x>.+)', self.snd),
            (r'set (?P<x>.+) (?P<y>.+)', self.set),
            (r'add (?P<x>.+) (?P<y>.+)', self.add),
            (r'mul (?P<x>.+) (?P<y>.+)', self.mul),
            (r'mod (?P<x>.+) (?P<y>.+)', self.mod),
            (r'rcv (?P<x>.+)', self.rcv),
            (r'jgz (?P<x>.+) (?P<y>.+)', self.jgz),
        )
        try:
            while True:
                operation = self.linesplitted[self.operation_pos]
                for pattern, f in patterns:
                    match = re.match(pattern, operation)
                    if match:
                        f(**match.groupdict())
                        self.operation_pos += 1
        except AssertionError:
            return self.last_sound


Day()
