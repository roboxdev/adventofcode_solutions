import re
from itertools import cycle

from aocframework import AoCFramework
from blist import blist


class Day(AoCFramework):
    test_cases = (
        ('9 players; last marble is worth 25 points', 32),
        ('10 players; last marble is worth 1618 points', 8317),
        ('13 players; last marble is worth 7999 points', 146373),
        ('17 players; last marble is worth 1104 points', 2764),
        ('21 players; last marble is worth 6111 points', 54718),
        ('30 players; last marble is worth 5807 points', 37305),
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
        for marble in range(1, points + 1):
            player = next(p)
            table_len = len(table)
            if marble % 23 == 0:
                score = marble
                if current_marble_index >= 7:
                    pop_index = current_marble_index - 7
                else:
                    print('-')
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
