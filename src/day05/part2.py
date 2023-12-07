from typing import Iterable

import tqdm

from day05.extraction import extract_map_and_seeds

from multiprocessing import Pool


def solve(puzzle_input: Iterable[str]) -> int:
    mapper, seed_ranges = extract_map_and_seeds(puzzle_input)

    seed_range_starts = seed_ranges[0::2]
    seed_range_lengths = seed_ranges[1::2]

    with Pool() as p:
        min_number_per_range = p.map(MapperProcessWrapper(mapper), list(zip(seed_range_starts, seed_range_lengths)))
    return min(min_number_per_range)


class MapperProcessWrapper:

    def __init__(self, mapper):
        self._mapper = mapper

    def __call__(self, seed_range):
        seed_range_start = seed_range[0]
        seed_range_length = seed_range[1]
        min_number = None
        for number in range(seed_range_start, seed_range_start + seed_range_length):
            if min_number is None:
                min_number = self._mapper(number)
            else:
                min_number = min(self._mapper(number), min_number)
        return min_number
