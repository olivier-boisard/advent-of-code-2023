import dataclasses
import re
from typing import Iterable, List


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


def solve(puzzle_input: Iterable[str]) -> int:
    all_maps, seeds = _extract_maps_and_seeds(puzzle_input)

    min_number = None
    for number in seeds:
        for range_map in all_maps:
            number = range_map[number]
        if min_number is None:
            min_number = number
        else:
            min_number = min(min_number, number)
    return min_number


def _extract_maps_and_seeds(puzzle_input):
    current_map_str = None
    current_ranges = []
    all_maps = []
    seeds = None
    for line in puzzle_input:
        if 'seeds:' in line:
            seeds = _extract_numbers(line)
        elif '-to-' in line:
            if current_map_str is not None:
                all_maps.append(MultiRangesMap(current_ranges))
            current_ranges = []
            current_map_str = line.split(' ')[0]
        else:
            numbers = _extract_numbers(line)
            if len(numbers) == 3:
                current_ranges.append(RangeMap(*numbers))
    all_maps.append(MultiRangesMap(current_ranges))
    if seeds is None:
        raise RuntimeError('No seeds found')
    return all_maps, seeds


def _extract_numbers(line: str) -> List[int]:
    return [int(i) for i in re.findall(r'\d+ ?', line)]
