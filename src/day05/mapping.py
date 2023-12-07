import dataclasses
from typing import List


@dataclasses.dataclass
class RangeMap:
    destination_range_start: int
    source_range_start: int
    range_length: int

    def __contains__(self, value: int) -> bool:
        return self.source_range_start <= value < self.source_range_start + self.range_length

    def __getitem__(self, item: int) -> int:
        if item not in self:
            raise IndexError(f'Unknown key {item}')
        return item - self.source_range_start + self.destination_range_start


class MultiRangesMap:
    def __init__(self, range_maps: List[RangeMap]):
        self._range_maps = range_maps

    def __getitem__(self, item: int) -> int:
        output = item
        for range_map in self._range_maps:
            if item in range_map:
                output = range_map[item]
                break
        return output
