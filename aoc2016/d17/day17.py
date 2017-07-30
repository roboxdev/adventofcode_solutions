from hashlib import md5

d_map = ('U', 'D', 'L', 'R')


class RoomState(tuple):
    def get_possible_moves(self):
        x, y, path_hash = self
        directions = md5(path_hash.encode('utf-8')).hexdigest()[:4]
        result = []
        for i, d in enumerate(directions):
            if d in '0123456789a':
                continue
            if i == 0:
                next_xy = x, y - 1
            elif i == 1:
                next_xy = x, y + 1
            elif i == 2:
                next_xy = x - 1, y
            elif i == 3:
                next_xy = x + 1, y
            if next_xy[0] not in range(4) or next_xy[1] not in range(4):
                continue
            result.append(RoomState((*next_xy, path_hash + d_map[i])))
        return result


class Solver(object):
    START = (0, 0)
    FINISH = (3, 3)

    def __init__(self, start_hash):
        self.start_hash = start_hash

    def go(self):
        a = RoomState((*self.START, self.start_hash))

        d = 0
        field = set()
        new_moves = [a]
        while True:
            temp = set()
            for f in new_moves:
                for move in f.get_possible_moves():
                    if move and move not in field:
                        temp.add(move)
                        if move[:2] == self.FINISH:
                            print('SOLUTION:', move)
                            return move[-1].lstrip(self.start_hash)
            new_moves = temp
            field |= temp
            d += 1
            print(len(new_moves), d)

        pass


if __name__ == '__main__':
    test = Solver('ihgpwlah')
    assert test.go() == 'DDRRRD'
    test = Solver('kglvqrro')
    assert test.go() == 'DDUDRLRRUDRD'
    test = Solver('ulqzkmiv')
    assert test.go() == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
    s = Solver('dmypynyp')
    print(s.go())
