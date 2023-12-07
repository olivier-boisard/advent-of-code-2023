import re
from functools import cache
from typing import List, Iterable, Callable, Any, Tuple

from day05.mapping import RangeMapper, MultipleMapper


def _chain(item: Any, funcs: Iterable[Callable[[Any], Any]]) -> Any:
    for func in funcs:
        item = func(item)
    return item


class Chain:

    def __init__(self, functions):
        self._functions = functions

    def __call__(self, v):
        for f in self._functions:
            v = f(v)
        return v


def extract_map_and_seeds(puzzle_input: Iterable[str]) -> Tuple[Callable[[int], int], Iterable[int]]:
    current_map_str = None
    current_ranges = []
    all_mappers = []
    seeds = None
    for line in puzzle_input:
        if 'seeds:' in line:
            seeds = _extract_numbers(line)
        elif '-to-' in line:
            if current_map_str is not None:
                all_mappers.append(MultipleMapper(current_ranges))
            current_ranges = []
            current_map_str = line.split(' ')[0]
        else:
            numbers = _extract_numbers(line)
            if len(numbers) == 3:
                current_ranges.append(RangeMapper(*numbers))
    all_mappers.append(MultipleMapper(current_ranges))
    if seeds is None:
        raise RuntimeError('No seeds found')

    return Chain(all_mappers), seeds


def _extract_numbers(line: str) -> List[int]:
    return [int(i) for i in re.findall(r'\d+ ?', line)]
