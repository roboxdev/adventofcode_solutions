from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''Generator A starts with 65
Generator B starts with 8921''', 309),
    )

    def go(self):
        GEN_A_FACTOR = 16807
        GEN_B_FACTOR = 48271
        DIVIDER = 2147483647
        JUDGE_PATIENCE = 5000000
        a, b = (int(v.split()[-1]) for v in self.linesplitted)
        gen_a_numbers = []
        gen_b_numbers = []
        a_go = True
        b_go = True
        while a_go or b_go:
            if len(gen_a_numbers) == JUDGE_PATIENCE:
                a_go = False
            if len(gen_b_numbers) == JUDGE_PATIENCE:
                b_go = False
            if a_go:
                a = a * GEN_A_FACTOR % DIVIDER
                if a % 4 == 0:
                    gen_a_numbers.append(a)
            if b_go:
                b = b * GEN_B_FACTOR % DIVIDER
                if b % 8 == 0:
                    gen_b_numbers.append(b)
        answer = sum(bin(a)[-16:] == bin(b)[-16:] for a, b in zip(gen_a_numbers, gen_b_numbers))
        return answer


Day()
