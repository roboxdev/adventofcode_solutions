from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('aa bb cc dd ee', 1),
        ('aa bb cc dd aa', 0),
        ('aa bb cc dd aaa', 1),
    )

    def go(self):
        counter = 0
        for line in self.linesplitted:
            splitted = line.split()
            if len(splitted) == len(set(splitted)):
                counter += 1
        return counter


Day()
