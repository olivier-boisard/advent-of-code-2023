from typing import Iterable

from day05.extraction import extract_map_and_seeds


def solve(puzzle_input: Iterable[str]) -> int:
    mapper, seed_ranges = extract_map_and_seeds(puzzle_input)

    seed_range_starts = seed_ranges[0::2]
    seed_range_lengths = seed_ranges[1::2]

    min_numbers = []
    for seed_range_start, seed_range_length in zip(seed_range_starts, seed_range_lengths):
        seed_range_stop = seed_range_start + seed_range_length
        min_numbers.append(min(*[mapper(number) for number in range(seed_range_start, seed_range_stop)]))
    return min(min_numbers)
