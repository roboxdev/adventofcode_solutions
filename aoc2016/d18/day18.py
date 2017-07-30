puzzle_input = '.^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^'


class Solver(object):
    def __init__(self, row, total_row_count):
        self.room = row
        self.row_len = len(row)
        self.total_row_count = total_row_count

    @staticmethod
    def is_trap(slice):
        left, center, right = slice
        if (left == '^' and center == '^' and right == '.') or \
                (left == '.' and center == '^' and right == '^') or \
                (left == '.' and center == '.' and right == '^') or \
                (left == '^' and center == '.' and right == '.'):
            return '^'
        return '.'

    def go(self):
        last_row = self.room
        row_counter = 1
        safe_tiles_counter = last_row.count('.')
        while row_counter < self.total_row_count:
            new_row = ''
            for i in range(self.row_len):
                if i == 0:
                    new_row += self.is_trap('.'+last_row[i:i+2])
                elif i == self.row_len - 1:
                    new_row += self.is_trap(last_row[i-1:i+1]+'.')
                else:
                    new_row += self.is_trap(last_row[i-1:i+2])
            safe_tiles_counter += new_row.count('.')
            row_counter += 1
            last_row = new_row
            if row_counter % 10000 == 0:
                print('{} out of {}'.format(row_counter, self.total_row_count))
        return safe_tiles_counter

if __name__ == '__main__':
    test = Solver('.^^.^.^^^^', 10)
    assert test.go() == 38
    s = Solver(puzzle_input, 40)
    print(s.go())
    s = Solver(puzzle_input, 400000)
    print(s.go())
