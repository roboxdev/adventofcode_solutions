import re
from collections import deque

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        # ('''s1,x3/4,pe/b''', ''),
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
        commands = [

        ]
        for operation in self.puzzle_input.split(','):
            for pattern, f in patterns:
                match = re.match(pattern, operation)
                if match:
                    commands.append((f, match.groupdict()))
        l = []
        s = set()
        b = 0
        while True:
            for f, a in commands:
                f(**a)
            l.append(self.s)
            s.add(self.s)
            if len(l) != len(s):
                print('bingo', b)
                break
            b += 1

        for _ in range(1000000000 % b - 1):
            for f, a in commands:
                f(**a)
        return self.s


Day()
