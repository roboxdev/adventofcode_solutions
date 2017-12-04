from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('abcde fghij', 1),
        ('abcde xyz ecdab', 0),
        ('a ab abc abd abf abj', 1),
        ('iiii oiii ooii oooi oooo', 1),
        ('oiii ioii iioi iiio', 0),
    )

    def go(self):
        counter = 0
        for line in self.linesplitted:
            p = [''.join(sorted(v)) for v in line.split()]
            if len(p) == len(set(p)):
                counter += 1
        return counter


Day()
