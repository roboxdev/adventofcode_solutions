from collections import Counter

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab''', 12
         ),)

    def go(self):
        doubles = 0
        triples = 0
        for box in self.linesplitted:
            counters = Counter(box).values()
            if 2 in counters:
                doubles += 1
            if 3 in counters:
                triples += 1
        return doubles * triples

Day()
