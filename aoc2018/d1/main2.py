from aocframework import AoCFramework

from itertools import cycle


class Day(AoCFramework):
    test_cases = (
        ('''+1
        -2
        +3
        +1''', 2
         ),
        ('''+1
            -1''', 0,),
        ('''+3
    +3
    +4
    -2
    -4''', 10,),
        ('''-6
    +3
    +8
    +5
    -6''', 5,),
        ('''+7
    +7
    -2
    -7
    -4''', 14,),
    )

    def go(self):
        frequency = 0
        checked_frequencies = {0}
        parsed = [int(op) for op in self.linesplitted]
        for op in cycle(parsed):
            frequency += op
            if frequency in checked_frequencies:
                return frequency
            checked_frequencies.add(frequency)
        print(checked_frequencies)
Day()
