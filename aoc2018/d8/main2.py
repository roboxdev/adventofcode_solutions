from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2''', 66),
    )

    def process(self, s):
        child_amount, metadata_entries_amount, *payload = s
        if child_amount == 0:
            sum_counter = sum(payload[:metadata_entries_amount])
            return payload[metadata_entries_amount:], sum_counter
        else:
            unprocessed_children = payload.copy()
            child_sums = [0]
            for i in range(child_amount+1):
                if unprocessed_children:
                    # metadata
                    if i == child_amount:
                        sum_indices = unprocessed_children[:metadata_entries_amount]
                        s = sum(list(child_sums[a] for a in sum_indices if a < len(child_sums)))
                        return unprocessed_children[metadata_entries_amount:], s
                    else:
                        unprocessed_children, sum_counter = self.process(unprocessed_children)
                        child_sums.append(sum_counter)

    def go(self):
        inted = [int(v) for v in self.puzzle_input.split()]
        _, sum_counter = self.process(inted)
        return sum_counter

Day()
