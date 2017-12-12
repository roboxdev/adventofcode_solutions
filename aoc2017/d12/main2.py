from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5''', 2),
    )

    def go(self):
        d = {k: v.split(', ') for k, v in map(lambda a: a.split(' <-> '), self.linesplitted)}
        answer = 0
        while d:
            passed = set()
            to_process = ['0'] if '0' in d else [list(d.keys())[0]]
            while to_process:
                t = tuple([x for x in to_process if x not in passed])
                to_process = []
                for i in t:
                    passed.add(i)
                    to_process += d[i]
            answer += 1
            for v in tuple(passed):
                del d[v]
        return answer


Day()
