from typing import Iterable

from day05.extraction import extract_map_and_seeds
from day05.mapping import Interval


def solve(puzzle_input: Iterable[str]) -> int:
    mapper, seed_intervals = extract_map_and_seeds(puzzle_input)

    seed_interval_starts = seed_intervals[0::2]
    seed_interval_lengths = seed_intervals[1::2]

    intervals = [Interval(start, start + length) for start, length in zip(seed_interval_starts, seed_interval_lengths)]
    intervals = sorted(intervals, key=lambda r: r.start)
    final_intervals = mapper(intervals)

    return final_intervals[0].start
