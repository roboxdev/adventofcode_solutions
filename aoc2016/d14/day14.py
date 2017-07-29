import re
from hashlib import md5


class Solver(object):
    def __init__(self, salt):
        self.salt = salt

    def go(self):
        keys = []
        hashes = ''
        for i in range(50000):
            input_string = '{}{}'.format(self.salt, i)
            hashes += '{}:{}\n'.format(i, md5(input_string.encode('utf-8')).hexdigest())
        match3 = re.findall(r'(\d+):.*?(.)(\2{2}).*?', hashes)
        match5 = re.findall(r'(\d+):.*?(.)(\2{4}).*?', hashes)
        for i, char, _ in match3:
            inted_i = int(i)
            filtered_match5 = list(filter(lambda match: match[1] == char and int(match[0]) in range(inted_i + 1, inted_i + 1001), match5))
            if filtered_match5 \
                    and i not in list(zip(*match5))[0]:
                keys.append(inted_i)
                print(len(keys), inted_i, hashes.splitlines()[inted_i], hashes.splitlines()[int(filtered_match5[0][0])], char)
                if len(keys) == 70:
                    break

    @staticmethod
    def encode(input_string):
        for _ in range(2017):
            input_string = md5(input_string.encode('utf-8')).hexdigest()
        return input_string

    def go2(self):
        keys = []
        hashes = ''
        f = open('./day14_hashes.txt', 'r+')
        try:
            hashes = f.read()
        except FileNotFoundError:
            for i in range(50000):
                input_string = '{}{}'.format(self.salt, i)
                hashes += '{}:{}\n'.format(i, self.encode(input_string))
            print(hashes, file=f)
        match3 = re.findall(r'(\d+):.*?(.)(\2{2}).*?', hashes)
        match5 = re.findall(r'(\d+):.*?(.)(\2{4}).*?', hashes)
        for i, char, _ in match3:
            inted_i = int(i)
            filtered_match5 = list(filter(lambda match: match[1] == char and int(match[0]) in range(inted_i + 1, inted_i + 1001), match5))
            if filtered_match5 \
                    and i not in list(zip(*match5))[0]:
                keys.append(inted_i)
                print(len(keys), inted_i, hashes.splitlines()[inted_i], hashes.splitlines()[int(filtered_match5[0][0])], char)
                if len(keys) == 70:
                    break

if __name__ == '__main__':
    test = Solver('abc')
    # test.go()
    test.go2()
    s = Solver('cuanljph')
    s.go()
    # s.go2()

    # not 23981, 24259, 24398, 24298
    # not 19903, 20188, 20307, 20351, 23670, 23695, 23769

    # 12012
    # 19730
    # 19860
