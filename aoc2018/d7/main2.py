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
Step F must be finished before step E can begin.''', 15),
    )

    def go(self):
        requirements = {k: '' for k in ascii_uppercase}
        delay = 0 if self.test else 60
        workers = 2 if self.test else 5
        worker_tasks = [('', 0)] * workers
        seconds_passed = 0
        win_condition = set()
        for req in self.linesplitted:
            m = re.match(r'Step (?P<req>\w) must be finished before step (?P<step>\w) can begin.', req)
            req, step = m.groups()
            win_condition = win_condition.union({req, step})
            requirements[step] += req
        path = ''

        while True:
            for letter in ''.join(sorted(list(win_condition))):
                if letter not in path \
                        and all(l in path for l in requirements[letter]) \
                        and letter not in list(zip(*worker_tasks))[0]:
                    time_to_process = delay + ascii_uppercase.index(letter) + 1
                    try:
                        free_worker_index = next(filter(lambda x: not x[1][1], enumerate(worker_tasks)))[0]
                        worker_tasks[free_worker_index] = (letter, time_to_process)
                    except StopIteration:
                        break

            for i, (letter, time) in enumerate(worker_tasks.copy()):
                if time > 1:
                    worker_tasks[i] = (letter, time-1)
                elif time == 1:
                    path += letter
                    worker_tasks[i] = ('', 0)
            seconds_passed += 1
            print(worker_tasks, path)
            if len(win_condition) == len(path):
                break

        if self.test:
            assert path == 'CABFDE'
        return seconds_passed

Day()
