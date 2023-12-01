import re
from typing import Iterable


def solve(puzzle_input: Iterable[str]) -> int:
    result = 0
    for line in puzzle_input:
        patterns = {
            'zero': '0',
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }
        left_digit = re.findall(r'|'.join(patterns.keys()) + r'|\d', line)[0]
        right_digit = re.findall(r'|'.join(patterns.keys())[::-1] + r'|\d', line[::-1])[0][::-1]
        number = patterns.get(left_digit, left_digit) + patterns.get(right_digit, right_digit)
        result += int(number)
    return result
