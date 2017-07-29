from hashlib import md5
import time

raw_puzzle_input = 'ffykfhsq'


class Solver(object):
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def go(self):
        pwd = ''
        counter = 0
        while True:
            input_string = '{}{}'.format(self.puzzle_input, counter)
            hash = md5(input_string.encode('utf-8')).hexdigest()
            if hash.startswith('00000'):
                pwd += hash[5]
                print(hash, pwd, counter)
            if len(pwd) == 8:
                return pwd
            counter += 1

    def go2(self):
        pwd = ['_' for _ in range(8)]
        counter = 0
        while True:
            input_string = '{}{}'.format(self.puzzle_input, counter)
            hash = md5(input_string.encode('utf-8')).hexdigest()
            if hash.startswith('00000') and hash[5] in '01234567' and pwd[int(hash[5])] == '_':
                pwd[int(hash[5])] = hash[6]
                print(hash, pwd, counter)
            if '_' not in pwd:
                return ''.join(pwd)
            counter += 1

if __name__ == '__main__':
    s = Solver(raw_puzzle_input)
    start = time.time()
    print(s.go(), time.time() - start)
    print(s.go2(), time.time() - start)
