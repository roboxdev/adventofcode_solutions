class Solver(object):
    def __init__(self, puzzle_input, length):
        self.puzzle_input = puzzle_input
        self.length = length

    def dragon_curved(self):
        result = self.puzzle_input
        while True:
            b = result
            b = b[::-1].replace('0', '2').replace('1', '0').replace('2', '1')
            result += '0' + b
            if len(result) >= self.length:
                return result

    def get_checksum(self, inp):
        a = [inp[i:i+2] for i in range(0, len(inp), 2)]
        b = ['1' if i == '11' or i == '00' else '0' for i in a]
        result = ''.join(b)
        if len(result) % 2 == 0:
            return self.get_checksum(result)
        else:
            return result

    def go(self):
        dragon_curved = self.dragon_curved()
        print(dragon_curved)
        checksum = self.get_checksum(dragon_curved[:self.length])
        print(checksum)
        return checksum

if __name__ == '__main__':
    test = Solver('10000', 20).go()
    assert test == '01100'
    puzzle_input = ('10011111011011001', 272)
    puzzle_input_2 = ('10011111011011001', 35651584)
    s = Solver(*puzzle_input).go()
    s2 = Solver(*puzzle_input_2).go()
