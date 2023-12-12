import re
from dataclasses import dataclass
from functools import reduce
from math import prod
from typing import Iterable, Iterator


@dataclass
class _RaceRecord:
    time: int
    distance: int


def solve(puzzle_input: Iterable[str]) -> int:
    race_records = _extract_race_records(puzzle_input)
    return prod(_compute_n_options_to_beat_record(race_record) for race_record in race_records)


def _extract_race_records(puzzle_input: Iterable[str]) -> Iterator[_RaceRecord]:
    puzzle_input = list(puzzle_input)
    times_str = re.findall(r'\d+ ?', puzzle_input[0])
    distances_str = re.findall(r'\d+ ?', puzzle_input[1])
    for time_str, distance_str in zip(times_str, distances_str):
        yield _RaceRecord(time=int(time_str), distance=int(distance_str))


def _compute_n_options_to_beat_record(race_record):
    half_time = race_record.time // 2
    upper_bound = half_time
    lower_bound = 0
    while lower_bound + 1 != upper_bound:
        current_speed = (lower_bound + upper_bound) // 2
        remaining_race_time = race_record.time - current_speed
        distance = remaining_race_time * current_speed
        if distance > race_record.distance:
            upper_bound = current_speed
        else:
            lower_bound = current_speed

    n_options = (half_time - upper_bound + 1) * 2
    if race_record.time % 2 == 0:
        n_options -= 1

    return n_options
