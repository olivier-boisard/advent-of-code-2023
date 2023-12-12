from dataclasses import dataclass


@dataclass
class RaceRecord:
    time: int
    distance: int


def compute_n_options_to_beat_record(race_record: RaceRecord) -> int:
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
