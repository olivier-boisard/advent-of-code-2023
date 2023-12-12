import re
from math import prod
from typing import Iterable, Iterator

from day06.race_records import compute_n_options_to_beat_record, RaceRecord


def solve(puzzle_input: Iterable[str]) -> int:
    race_records = _extract_race_records(puzzle_input)
    return prod(compute_n_options_to_beat_record(race_record) for race_record in race_records)


def _extract_race_records(puzzle_input: Iterable[str]) -> Iterator[RaceRecord]:
    puzzle_input = list(puzzle_input)
    times_str = re.findall(r'(\d+) ?', puzzle_input[0])
    distances_str = re.findall(r'(\d+) ?', puzzle_input[1])
    for time_str, distance_str in zip(times_str, distances_str):
        yield RaceRecord(time=int(time_str), distance=int(distance_str))


