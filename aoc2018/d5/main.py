from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''dabAcCaCBAcCcaDA''', 10),
    )

    @staticmethod
    def make_pairs(s):
        return zip(s, s[1:])

    def go(self):
        result = self.puzzle_input
        while True:
            temp = result
            pairs = self.make_pairs(result)
            pass
            for n, m in pairs:
                if n.lower() == m.lower() and n != m:
                    result = result.replace(n+m, '')
                    break
            if len(temp) == len(result):
                return len(result)


Day()
