import re
from collections import defaultdict
from pprint import pprint

import sympy
from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
    )

    def set(self, x, y=None, static_y=None):
        self.d[x] = static_y if static_y is not None else self.d[y]

    def sub(self, x, y=None, static_y=None):
        self.d[x] -= static_y if static_y is not None else self.d[y]

    def mul(self, x, y=None, static_y=None):
        self.d[x] *= static_y if static_y is not None else self.d[y]

    def jnz(self, x=None, static_x=None, y=None, static_y=None):
        x = static_x if static_x is not None else self.d[x]
        y = static_y if static_y is not None else self.d[y]
        if x != 0:
            self.operation_pos += y - 1
        assert self.operation_pos >= 0

    def check(self, d):
        return all([self.d[k] == v for k, v in d.items()])

    def go(self):
        self.d = defaultdict(int)
        self.d['a'] = 1
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
                    kwargs = match.groupdict().copy()
                    if not kwargs['y'].isalpha():
                        kwargs['static_y'] = int(kwargs['y'])
                        del kwargs['y']
                    if f == self.jnz and not kwargs['x'].isalpha():
                        kwargs['static_x'] = int(kwargs['x'])
                        del kwargs['x']
                    operations.append((f, kwargs))
        while True:
            f, kwargs = operations[self.operation_pos]
            f(**kwargs)
            if self.operation_pos == 8:
                return len(tuple(filter(
                    lambda v: not sympy.isprime(v),
                    tuple(range(self.d['b'], self.d['c'] + 1, 17)[:1001])
                )))
            self.operation_pos += 1


Day()
