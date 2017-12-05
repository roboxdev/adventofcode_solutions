from pathlib import Path
from pprint import pprint
import requests


class AoCFramework(object):
    session_token = ''
    raw_puzzle_input = ''
    test_cases = ('test case placeholder', 0),
    known_result = None

    def get_session_token(self, token_path):
        with open(token_path) as f:
            self.session_token = f.read()

    def get_puzzle_input(self, puzzle_input_path):
        try:
            with open(puzzle_input_path) as f:
                self.raw_puzzle_input = f.read()
        except FileNotFoundError:
            with open(puzzle_input_path, 'w') as f:
                res = requests.get(
                    url=f'http://adventofcode.com/{self.year}/day/{self.day}/input',
                    cookies={'session': self.session_token}
                )
                f.write(res.text)
                self.raw_puzzle_input = res.text

    def __init__(self, puzzle_input=None):
        # p = Path(sys.argv[0])
        p = Path(__import__(type(self).__module__).__file__)
        *root, aoc_year, d_day, _ = p.parts
        self.year = aoc_year[-4:]
        self.day = d_day[1:]
        if puzzle_input is None:
            self.get_session_token(p.joinpath(*root, 'session_token'))
            self.get_puzzle_input(p.joinpath(*p.parts[:-1], 'raw_input.txt'))
        else:
            self.raw_puzzle_input = puzzle_input
        self.linesplitted = self.raw_puzzle_input.splitlines()
        if puzzle_input is None:
            pprint(self.linesplitted)
            print('***')
            self.run_tests()
        self.result = self.go()
        if puzzle_input is None:
            print('Answer:', self.result)
            if self.known_result is not None:
                if self.result == self.known_result:
                    print('You are right!')
                else:
                    print('You are wrong (answer must be %s)' % self.known_result)
        pass

    def run_tests(self):
        for case, result in self.test_cases:
            try:
                day = type(self)(case)
                assert day.result == result
                print(f'Test OK: {case} == {result}')
            except AssertionError:
                print(f'Test fail: {case} == {day.result} != {result}')

    def go(self):
        raise NotImplementedError
