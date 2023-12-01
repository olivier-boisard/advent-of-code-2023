import re
from typing import Iterable


def solve(puzzle_input: Iterable[str]) -> int:
    result = 0
    for line in puzzle_input:
        numbers = re.findall(r'\d', line)
        result += int(numbers[0] + numbers[-1])
    return result
