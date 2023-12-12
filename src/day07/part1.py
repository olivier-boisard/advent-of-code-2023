from typing import Iterable

from day07.hand import standard_strength_computer, run_game


def solve(puzzle_input: Iterable[str]) -> int:
    return run_game(puzzle_input, standard_strength_computer)