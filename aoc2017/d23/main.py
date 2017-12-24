import re
from collections import defaultdict

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
    )

    def set(self, x, y):
        self.d[x] = self.d[y] if y.isalpha() else int(y)

    def sub(self, x, y):
        self.d[x] -= self.d[y] if y.isalpha() else int(y)

    def mul(self, x, y):
        self.mul_counter += 1
        self.d[x] *= self.d[y] if y.isalpha() else int(y)

    def jnz(self, x, y):
        x = self.d[x] if x.isalpha() else int(x)
        y = self.d[y] if y.isalpha() else int(y)
        if x != 0:
            self.operation_pos += y - 1
        assert self.operation_pos >= 0

    def go(self):
        self.mul_counter = 0
        self.d = defaultdict(int)
        self.operation_pos = 0
        patterns = (
            (r'set (?P<x>.+) (?P<y>.+)', self.set),
            (r'sub (?P<x>.+) (?P<y>.+)', self.sub),
            (r'mul (?P<x>.+) (?P<y>.+)', self.mul),
            (r'jnz (?P<x>.+) (?P<y>.+)', self.jnz),
        )
        operations = []
        for operation in self.linesplitted:
            for pattern, f in patterns:
                match = re.match(pattern, operation)
                if match:
                    operations.append((f, match.groupdict()))
        try:
            while True:
                f, kwargs = operations[self.operation_pos]
                f(**kwargs)
                self.operation_pos += 1
        except IndexError:
            return self.mul_counter


Day()
