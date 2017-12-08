from aocframework import AoCFramework
import re


class Day(AoCFramework):
    test_cases = (
    )
    registers = {}
    historical_max = 0

    def do_operation(self, register, operation, amount, c_register, c_sign, c_amount):
        amount, c_amount = int(amount), int(c_amount)
        self.registers.setdefault(register, 0)
        self.registers.setdefault(c_register, 0)
        comparison_signs = {
            '!=': lambda a, b: a != b,
            '==': lambda a, b: a == b,
            '<=': lambda a, b: a <= b,
            '>=': lambda a, b: a >= b,
            '<': lambda a, b: a < b,
            '>': lambda a, b: a > b,
        }
        if comparison_signs[c_sign](self.registers[c_register], c_amount):
            self.registers[register] += amount if operation == 'inc' else -amount
            self.historical_max = max(self.registers[register], self.historical_max)
        pass

    def go(self):
        pattern = r'(?P<register>.+) (?P<operation>inc|dec) (?P<amount>.+) if (?P<c_register>.+) (?P<c_sign>.+) (?P<c_amount>.+)'
        for command in self.linesplitted:
            match = re.match(pattern, command)
            self.do_operation(**match.groupdict())
        answer = self.historical_max
        return answer


Day()
