from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''Generator A starts with 65
Generator B starts with 8921''', 588),
    )

    def go(self):
        answer = 0
        GEN_A_FACTOR = 16807
        GEN_B_FACTOR = 48271
        DIVIDER = 2147483647
        a, b = (int(v.split()[-1]) for v in self.linesplitted)
        for i in range(40000000):
            a = a * GEN_A_FACTOR % DIVIDER
            b = b * GEN_B_FACTOR % DIVIDER
            answer += bin(a)[-16:] == bin(b)[-16:]
        return answer


Day()
