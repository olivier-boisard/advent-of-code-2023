import re
from typing import List

from day05.mapping import MultiRangesMap, RangeMap


def extract_maps_and_seeds(puzzle_input):
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
