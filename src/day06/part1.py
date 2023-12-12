import re
from dataclasses import dataclass
from typing import Iterable


@dataclass
class _RaceRecord:
    time: int
    distance: int


def solve(puzzle_input: Iterable[str]) -> int:
    puzzle_input = list(puzzle_input)
    times_str = re.findall(r'\d+ ?', puzzle_input[0])
    distances_str = re.findall(r'\d+ ?', puzzle_input[1])
    race_records = []
    for time_str, distance_str in zip(times_str, distances_str):
        race_records.append(_RaceRecord(time=int(time_str), distance=int(distance_str)))

    n_options = 1
    for race_record in race_records:
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
        factor = (half_time - upper_bound + 1) * 2
        if race_record.time % 2 == 0:
            factor -= 1
        n_options *= factor
    return n_options
