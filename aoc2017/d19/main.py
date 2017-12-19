import numpy as np

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ ''', 'ABCDEF'
         ),
    )

    directions = (
        complex(-1, 0),
        complex(0, 1),
        complex(1, 0),
        complex(0, -1),
    )

    def straight(self, d):
        return self.directions[d]

    def cw(self, d):
        return self.directions[(d + 1) if d != 3 else 0]

    def ccw(self, d):
        return self.directions[(d - 1) if d != 0 else 3]

    @staticmethod
    def is_coord_valid(c, ar):
        if min(c.real, c.imag) < 0:
            return False
        try:
            ar[int(c.real), int(c.imag)]
        except IndexError:
            return False
        return True

    def go(self):
        answer_set = set(filter(str.isalpha, self.puzzle_input))
        answer = ''
        l = list(map(list, self.linesplitted))
        ar = np.array(l)
        assert ar.ndim == 2
        pos = complex(0, list(ar[0]).index('|'))
        assert ar[int(pos.real), int(pos.imag)] == '|'
        direction = 2
        while True:
            current_symb = ar[int(pos.real), int(pos.imag)]
            if current_symb.isalpha():
                answer += current_symb
                if len(answer) == len(answer_set):
                    return answer
            if current_symb == '+':
                cw_coord = self.cw(direction) + pos
                if self.is_coord_valid(cw_coord, ar):
                    cw_symb = ar[int(cw_coord.real), int(cw_coord.imag)]
                    if cw_symb != ' ':
                        pos = cw_coord
                        direction = direction + 1 if direction != 3 else 0
                        continue
                ccw_coord = self.ccw(direction) + pos
                if self.is_coord_valid(ccw_coord, ar):
                    ccw_symb = ar[int(ccw_coord.real), int(ccw_coord.imag)]
                    if ccw_symb != '':
                        pos = ccw_coord
                        direction = direction - 1 if direction != 0 else 3
                        continue
            else:
                straight_coord = self.straight(direction) + pos
                pos = straight_coord
                continue


Day()
