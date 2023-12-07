from typing import Iterable

from day05.extraction import extract_map_and_seeds


def solve(puzzle_input: Iterable[str]) -> int:
    mapper, seeds = extract_map_and_seeds(puzzle_input)
    return min(*[mapper(number) for number in seeds])
