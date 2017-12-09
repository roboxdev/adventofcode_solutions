from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''{}''', 1),
        ('''{{{}}}''', 6),
        ('''{{},{}}''', 5),
        ('''{{{},{},{{}}}}''', 16),
        ('''{<a>,<a>,<a>,<a>}''', 1),
        ('''{{<ab>},{<ab>},{<ab>},{<ab>}}''', 9),
        ('''{{<!!>},{<!!>},{<!!>},{<!!>}}''', 9),
        ('''{{<a!>},{<a!>},{<a!>},{<ab>}}''', 3),
    )

    @property
    def exclamation_cleaned(self):
        s = self.puzzle_input
        pos = 0
        while pos < len(s):
            if s[pos] == '!':
                s = s[:pos] + '__' + s[pos+2:]
                pass
            pos += 1
        return s

    @property
    def without_garbage(self):
        s = self.exclamation_cleaned
        pos = 0
        while pos < len(s):
            if s[pos] == '<':
                closing_tag_pos = s.find('>', pos)
                s = s[:pos] + '=' * (closing_tag_pos - pos + 1) + s[closing_tag_pos + 1:]
            pos += 1
        return s

    def go(self):
        score = 0
        s = self.without_garbage
        while '}' in s:
            closing_tag = s.find('}')
            opening_tag = s.rfind('{', 0, closing_tag)
            new_s = s[:opening_tag] + '[' + s[opening_tag + 1:closing_tag] + ']' + s[closing_tag + 1:]
            score += s[:opening_tag + 1].count('{')
            s = new_s
        return score


Day()
