from typing import Iterable

from day05.extraction import extract_maps_and_seeds


def solve(puzzle_input: Iterable[str]) -> int:
    all_maps, seeds = extract_maps_and_seeds(puzzle_input)

    min_number = None
    for number in seeds:
        for range_map in all_maps:
            number = range_map[number]
        if min_number is None:
            min_number = number
        else:
            min_number = min(min_number, number)
    return min_number
