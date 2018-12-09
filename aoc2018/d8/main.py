from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2''', 138),
    )
    sum_counter = 0

    def process(self, s):
        child_amount, metadata_entries_amount, *payload = s
        unprocessed_children = payload.copy()
        for i in range(child_amount+1):
            if unprocessed_children:
                # metadata
                if i == child_amount:
                    self.sum_counter += sum(unprocessed_children[:metadata_entries_amount])
                    return unprocessed_children[metadata_entries_amount:]
                else:
                    unprocessed_children = self.process(unprocessed_children)

    def go(self):
        inted = [int(v) for v in self.puzzle_input.split()]
        self.process(inted)
        return self.sum_counter

Day()
