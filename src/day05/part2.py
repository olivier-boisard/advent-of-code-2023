from typing import Iterable

import tqdm

from day05.extraction import extract_maps_and_seeds


def solve(puzzle_input: Iterable[str]) -> int:
    all_maps, seed_ranges = extract_maps_and_seeds(puzzle_input)

    seed_range_starts = seed_ranges[0::2]
    seed_range_lengths = seed_ranges[1::2]

    min_number = None
    for seed_range_start, seed_range_length in zip(seed_range_starts, seed_range_lengths):
        for number in tqdm.tqdm(range(seed_range_start, seed_range_start + seed_range_length)):
            for range_map in all_maps:
                number = range_map[number]
            if min_number is None:
                min_number = number
            else:
                min_number = min(min_number, number)
    return min_number
