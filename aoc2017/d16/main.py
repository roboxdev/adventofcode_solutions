import re
from collections import deque

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''s1,x3/4,pe/b''', 'baedc'),
    )

    def spin(self, x):
        d = deque(self.s)
        d.rotate(int(x))
        self.s = ''.join(d)

    def exchange(self, x, y):
        x, y = int(x), int(y)
        l = list(self.s)
        l[x], l[y] = l[y], l[x]
        self.s = ''.join(l)

    def partner(self, x, y):
        l = list(self.s)
        x, y = l.index(x), l.index(y)
        l[x], l[y] = l[y], l[x]
        self.s = ''.join(l)

    def go(self):
        self.s = 'abcde' if self.test else 'abcdefghijklmnop'
        patterns = (
            (r's(?P<x>.+)', self.spin),
            (r'x(?P<x>.+)/(?P<y>.+)', self.exchange),
            (r'p(?P<x>.+)/(?P<y>.+)', self.partner),
        )
        for operation in self.puzzle_input.split(','):
            for pattern, f in patterns:
                match = re.match(pattern, operation)
                if match:
                    f(**match.groupdict())
        return self.s


Day()
