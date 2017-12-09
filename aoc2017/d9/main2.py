from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''<>''', 0),
        ('''<random characters>''', 17),
        ('''<<<<>''', 3),
        ('''<{!>}>''', 2),
        ('''<!!>''', 0),
        ('''<!!!>>''', 0),
        ('''<{o"i!a,<{i<a>''', 10),
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

    def go(self):
        s = self.exclamation_cleaned.replace('__', '')
        pos = 0
        while pos < len(s):
            if s[pos] == '<':
                closing_tag_pos = s.find('>', pos)
                s = s[:pos] + '=' * (closing_tag_pos - pos - 1) + s[closing_tag_pos + 1:]
            pos += 1
        garbage_counter = s.count('=')
        return garbage_counter


Day()
