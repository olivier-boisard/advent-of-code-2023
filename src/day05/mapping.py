from dataclasses import dataclass


@dataclass
class IntervalMapperMixin:
    destination_interval_start: int
    source_interval_start: int
    interval_length: int
