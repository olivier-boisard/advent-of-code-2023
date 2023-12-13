from typing import Iterable

from day07.hand import standard_type_extractor, HandStrengthComputer
from day07.game import run


def solve(puzzle_input: Iterable[str]) -> int:
    figure_to_int_mapping = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return run(
        puzzle_input,
        HandStrengthComputer(figure_to_int_mapping)
    )
