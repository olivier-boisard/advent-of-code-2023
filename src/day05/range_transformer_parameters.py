from dataclasses import dataclass


@dataclass
class RangeTransformerParameters:
    destination_interval_start: int
    source_interval_start: int
    interval_length: int
