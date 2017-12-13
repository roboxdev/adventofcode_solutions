from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''0: 3
1: 2
4: 4
6: 4''', 24),
    )

    def go(self):
        t = tuple((int(depth), int(r)) for depth, r in (v.split(': ') for v in self.linesplitted))
        d = {k: v for k, v in t}
        severity = 0
        for picosecond in range(t[-1][0]+1):
            if picosecond not in d:
                continue
            r = d[picosecond]
            scanner_pos = picosecond % (r * 2 - 2)
            if scanner_pos == 0:
                severity += picosecond * r
        return severity


Day()
