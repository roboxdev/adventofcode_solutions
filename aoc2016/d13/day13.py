import numpy as np


class Solver(object):
    def __init__(self, favorite_number, target):
        self.start = (1, 1)
        self.favorite_number = favorite_number
        self.target = target
        self.room = np.zeros((target[0]+10, target[1]+10, ), np.int)

    def is_obstacle(self, x, y):
        a = x*x + 3*x + 2*x*y + y + y*y + self.favorite_number
        binary_string = "{0:b}".format(a)
        return -2 if binary_string.count('1') % 2 else -1

    def go(self):
        for (x, y), value in np.ndenumerate(self.room, ):
            self.room[x, y] = self.is_obstacle(x, y)
        self.room[self.start] = 0
        d = 0
        np.set_printoptions(threshold=np.nan)
        coordinates = 0
        while True:
            current_cubicles = list(zip(*np.nonzero(self.room == d)))
            if not current_cubicles:
                print(d, 'No path found')
                break
            for x, y in current_cubicles:
                nearby_cubicle_coords = ((x-1, y), (x, y-1), (x+1, y), (x, y+1))
                for x, y in nearby_cubicle_coords:
                    if 0 <= x < self.room.shape[0] and 0 <= y < self.room.shape[1] and self.room[x, y] == -1:
                        self.room[x, y] = d + 1
                        coordinates += 1 if d <= 50 else 0
                    pass
            if self.room[self.target] > 0:
                print('SOLUTION', self.room[self.target])
                break
            d += 1
        print(self.room.T)
        print('SOLUTION 2', coordinates)


if __name__ == '__main__':
    # test = Solver(favorite_number=10, target=(7, 4))
    # test.go()
    # s = Solver(favorite_number=1362, target=(31, 39))
    s = Solver(favorite_number=1352, target=(31, 39))
    s.go()
