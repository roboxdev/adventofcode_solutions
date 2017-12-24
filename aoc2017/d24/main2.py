from itertools import chain

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''0/2
        2/2
        2/3
        3/4
        3/5
        0/1
        10/1
        9/10''', 19),
    )

    def find(self, last_connector, components, ch=()):
        connectors = tuple(set(self.d[last_connector]) - set(ch))
        if connectors:
            for c1, c2 in connectors:
                connector = c1 if c1 == c2 else tuple({c1, c2} - {last_connector})[0]
                new_comps = list(filter(lambda v: v != (c1, c2), components))
                assert len(new_comps) + 1 == len(components)
                new_ch = ch + ((c1, c2), )
                self.find(connector, new_comps, new_ch)
        else:
            if len(ch) >= self.max_length:
                self.max_length = len(ch)
                self.max_strength = sum(map(sum, ch))

    def go(self):
        self.max_strength = 0
        self.max_length = 0
        components = [tuple(map(int, c.split('/'))) for c in self.linesplitted]
        keys = tuple(set(chain(*components)))
        self.d = {k: tuple(filter(lambda v: k in v, components)) for k in keys}
        start = 0
        self.find(start, components)

        return self.max_strength

Day()
