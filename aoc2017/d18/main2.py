from collections import defaultdict

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d''', 3),
    )

    def intify(self, v, p):
        return self.d[p][v] if v.isalpha() else int(v)

    def snd(self, x, p):
        self.queues[int(not p)].append(self.d[p][x] if x.isalpha() else int(x))
        if p == 1:
            self.answer += 1

    def set(self, x, y, p):
        self.d[p][x] = self.intify(y, p)

    def add(self, x, y, p):
        self.d[p][x] += self.intify(y, p)

    def mul(self, x, y, p):
        self.d[p][x] *= self.intify(y, p)

    def mod(self, x, y, p):
        self.d[p][x] %= self.intify(y, p)

    def rcv(self, x, p):
        assert self.queues[p]
        self.d[p][x] = self.queues[p].pop(0)

    def jgz(self, x, y, p):
        if self.intify(x, p) > 0:
            self.operation_pos[p] += self.intify(y, p) - 1

    def program(self, p):
        while True:
            f, kwargs = self.operations[self.operation_pos[p]]
            f(**kwargs, p=p)
            self.operation_pos[p] += 1

    def go(self):
        patterns = (
            (r'snd (?P<x>.+)', self.snd),
            (r'set (?P<x>.+) (?P<y>.+)', self.set),
            (r'add (?P<x>.+) (?P<y>.+)', self.add),
            (r'mul (?P<x>.+) (?P<y>.+)', self.mul),
            (r'mod (?P<x>.+) (?P<y>.+)', self.mod),
            (r'rcv (?P<x>.+)', self.rcv),
            (r'jgz (?P<x>.+) (?P<y>.+)', self.jgz),
        )
        self.d = defaultdict(int), defaultdict(int)
        self.d[0]['p'] = 0
        self.d[1]['p'] = 1
        self.operation_pos = [0, 0]
        self.queues = ([], [])
        self.answer = 0
        self.operations = self.get_operations(patterns)
        current_proccess = 0
        while True:
            try:
                self.program(current_proccess)
            except AssertionError:
                current_proccess = int(not current_proccess)
                if not any(self.queues):
                    return self.answer
            assert self.answer < 7000


Day()
