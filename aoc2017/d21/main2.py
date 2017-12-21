import numpy as np

from aocframework import AoCFramework

MAGIC_STABILITY_REFERENCE = 1000  # Hope that's enough


class Day(AoCFramework):
    test_cases = (
)

    @staticmethod
    def np_to_line(ar):
        flat = ''.join(list(np.ndarray.flatten(ar)))
        if len(flat) == 4:
            return '/'.join((flat[:2], flat[2:]))
        elif len(flat) == 9:
            return '/'.join((flat[:3], flat[3:6], flat[6:]))
        else:
            raise ValueError

    @staticmethod
    def line_to_np(s):
        ar = np.array(list(map(list, s.split('/'))))
        assert ar.ndim == 2
        return ar

    def go(self):
        iterations = 18
        start = '''.#.
..#
###'''
        image = np.array(list(map(list, start.splitlines())))
        rulebook = {}
        rulebook_rotations = {}
        for k, v in map(lambda s: s.split(' => '), self.linesplitted):
            np_k, np_v = self.line_to_np(k), self.line_to_np(v)
            np_k_90 = np.rot90(np_k)
            np_k_180 = np.rot90(np_k_90)
            np_k_270 = np.rot90(np_k_180)
            np_k_f = np.fliplr(np_k)
            np_k_f_90 = np.rot90(np_k_f)
            np_k_f_180 = np.rot90(np_k_f_90)
            np_k_f_270 = np.rot90(np_k_f_180)
            rulebook.update({
                self.np_to_line(np_k): np_v,
            })
            rulebook_rotations.update({
                self.np_to_line(np_k_90): np_v,
                self.np_to_line(np_k_180): np_v,
                self.np_to_line(np_k_270): np_v,
                self.np_to_line(np_k_f): np_v,
                self.np_to_line(np_k_f_90): np_v,
                self.np_to_line(np_k_f_180): np_v,
                self.np_to_line(np_k_f_270): np_v,
            })
        rulebook_rotations.update(rulebook)
        rulebook = rulebook_rotations
        del rulebook_rotations
        for _ in range(iterations):
            if len(image) % 2 == 0:
                chunks_count = len(image) // 2
            elif len(image) % 3 == 0:
                chunks_count = len(image) // 3
            else:
                raise ValueError
            if chunks_count == 1:
                image = rulebook[self.np_to_line(image)]
                continue
            t = [np.hsplit(v, chunks_count) for v in (np.vsplit(image, chunks_count))]
            new_image = [[rulebook[self.np_to_line(j)] for j in i] for i in t]
            image = np.block(new_image)
        return str(tuple(np.ndarray.flatten(image))).count('#')


Day()
