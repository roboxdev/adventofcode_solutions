from aocframework import AoCFramework
import string


class Day(AoCFramework):
    test_cases = (
        ('''dabAcCaCBAcCcaDA''', 4),
    )

    @staticmethod
    def make_pairs(s):
        return zip(s, s[1:])

    def find_polymer_length(self, s):
        result = s
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

    def go(self):
        result = {}
        for letter in string.ascii_lowercase:
            trimmed = self.puzzle_input.replace(letter, '').replace(letter.upper(), '')
            result[letter] = self.find_polymer_length(trimmed)
            print(letter)
        return min(result.items(), key=lambda x: x[1])[1]


Day()
