from typing import Iterable

from day07.game import run
from day07.hand import HandStrengthComputer


def solve(puzzle_input: Iterable[str]) -> int:
    figure_to_int_mapping = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return run(
        puzzle_input,
        HandStrengthComputer(figure_to_int_mapping)
    )
