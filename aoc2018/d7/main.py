import re
from string import ascii_uppercase
from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.''', 'CABDFE'),
    )

    def go(self):
        requirements = {k: '' for k in ascii_uppercase}
        win_condition = set()
        for req in self.linesplitted:
            m = re.match(r'Step (?P<req>\w) must be finished before step (?P<step>\w) can begin.', req)
            req, step = m.groups()
            win_condition = win_condition.union({req, step})
            requirements[step] += req
        path = ''
        while True:
            for letter in ''.join(sorted(list(win_condition))):
                if letter not in path and all(l in path for l in requirements[letter]):
                    path += letter
                    break
            if len(win_condition) == len(path):
                break
        return path

Day()
