from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5''', 6),
    )

    def go(self):
        d = {k: v.split(', ') for k, v in map(lambda a: a.split(' <-> '), self.linesplitted)}
        passed = set()
        to_process = ['0']
        while to_process:
            t = tuple([x for x in to_process if x not in passed])
            to_process = []
            for i in t:
                passed.add(i)
                to_process += d[i]
        return len(passed)


Day()
