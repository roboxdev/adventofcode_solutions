import itertools

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz''', 'fgij'
         ),)

    def compare(self, a, b):
        union = ''
        was_different_char = False
        for n, m in zip(a, b):
            if n == m:
                union += n
            elif not was_different_char:
                was_different_char = True
            else:
                return None
        print(union, a, b)
        return union

    def go(self):
        for pair in itertools.combinations(self.linesplitted, 2):
            result = self.compare(*pair)
            if result:
                return result

Day()
