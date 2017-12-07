from aocframework import AoCFramework


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
        cntj (57)''', 'tknk'),
    )

    def go(self):
        all_names = [line.split()[0] for line in self.linesplitted]
        right_names = sum([line.split('-> ')[1].split(', ') for line in self.linesplitted if '->' in line], [])
        return tuple(set(all_names) - set(right_names))[0]


Day()
