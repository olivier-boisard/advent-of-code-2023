from typing import Iterable

from day07.hand import standard_strength_computer, run_game


def solve(puzzle_input: Iterable[str]) -> int:
    return run_game(puzzle_input, standard_strength_computer, {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})
