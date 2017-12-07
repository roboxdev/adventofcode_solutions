from aocframework import AoCFramework
from collections import Counter

class Day(AoCFramework):
    test_cases = (
        ('''pbga (66)
        xhth (57)
        ebii (61)
        havc (66)
        ktlj (57)
        fwft (72) -> ktlj, cntj, xhth
        qoyq (66)
        padx (45) -> pbga, havc, qoyq
        tknk (41) -> ugml, padx, fwft
        jptl (61)
        ugml (68) -> gyxo, ebii, jptl
        gyxo (61)
        cntj (57)''', 60),
    )

    def find_balance(self, w):
        d = {k: v for k, v in w}
        most_common, *_, least_common = Counter(list(zip(*w))[0]).most_common()
        diff = most_common[0] - least_common[0]
        raise Exception(d[least_common[0]]+diff)

    def get_weight(self, name):
        try:
            vals = self.right_names[name]
        except KeyError:
            return self.weights[name]

        w = list(map(self.get_weight, vals))
        b = [v[0] if isinstance(v, tuple) else v for v in w]
        if min(b) == max(b):
            return sum(b)+self.weights[name], self.weights[name]
        else:
            self.find_balance(w)

    def root(self):
        all_names = [line.split()[0] for line in self.linesplitted]
        right_names = sum([line.split('-> ')[1].split(', ') for line in self.linesplitted if '->' in line], [])
        return tuple(set(all_names) - set(right_names))[0]

    def go(self):
        all_names = [line.split()[0] for line in self.linesplitted]
        self.right_names = {line.split()[0]: line.split('-> ')[1].split(', ') for line in self.linesplitted if '->' in line}
        self.weights = {line.split()[0]: int(line[line.find('(')+1:line.find(')')]) for line in self.linesplitted}
        try:
            self.get_weight(self.root())
        except Exception as e:
            print(e)
            return int(str(e))


Day()
