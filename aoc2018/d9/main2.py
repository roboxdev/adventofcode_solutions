import re
from itertools import cycle

from aocframework import AoCFramework
from blist import blist


class Day(AoCFramework):
    test_cases = (
    )

    def go(self):
        print(self.linesplitted)
        m = re.match(
            r'(\d+) players; last marble is worth (\d+) points',
            self.puzzle_input
        )
        players, points = map(int, m.groups())
        scoreboard = [0] * players
        table = blist([0])
        p = cycle(range(players))
        current_marble_index = 0
        for marble in range(1, (points * 100) + 1):
            player = next(p)
            table_len = len(table)
            if marble % 23 == 0:
                score = marble
                if current_marble_index >= 7:
                    pop_index = current_marble_index - 7
                else:
                    pop_index = table_len + (current_marble_index - 7)
                popped_marble = table.pop(pop_index)
                scoreboard[player] += score + popped_marble
                current_marble_index = pop_index
            else:
                insert_index = 1 if table_len == (current_marble_index + 1) else current_marble_index + 2
                table.insert(insert_index, marble)
                current_marble_index = insert_index

        return max(scoreboard)

Day()
