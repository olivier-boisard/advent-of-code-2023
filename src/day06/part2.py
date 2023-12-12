import re
from typing import Iterable

from day06.race_records import compute_n_options_to_beat_record, RaceRecord


def solve(puzzle_input: Iterable[str]) -> int:
    race_record = _extract_race_records(puzzle_input)
    return compute_n_options_to_beat_record(race_record)


def _extract_race_records(puzzle_input: Iterable[str]) -> RaceRecord:
    puzzle_input = list(puzzle_input)
    return RaceRecord(
        time=int(''.join(re.findall(r'(\d+) ?', puzzle_input[0]))),
        distance=int(''.join(re.findall(r'(\d+) ?', puzzle_input[1])))
    )
