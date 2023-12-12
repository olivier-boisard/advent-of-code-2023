import re
from typing import List, Iterable, Callable, Any, Tuple, TypeVar

from day05.range_transformer_parameters import RangeTransformerParameters


def _chain(item: Any, funcs: Iterable[Callable[[Any], Any]]) -> Any:
    for func in funcs:
        item = func(item)
    return item


T = TypeVar('T')


def extract_map_and_seeds(
        puzzle_input: Iterable[str],
        intervals_mapper_factory: Callable[[Iterable[RangeTransformerParameters]], Callable[[T], T]]
) -> Tuple[Callable[[T], T], Iterable[int]]:
    current_map_str = None
    current_interval_mappers = []
    all_mappers = []
    seeds = None
    for line in puzzle_input:
        if 'seeds:' in line:
            seeds = _extract_numbers(line)
        elif '-to-' in line:
            if current_map_str is not None:
                all_mappers.append(intervals_mapper_factory(current_interval_mappers))
            current_interval_mappers = []
            current_map_str = line.split(' ')[0]
        else:
            numbers = _extract_numbers(line)
            if len(numbers) == 3:
                current_interval_mappers.append(RangeTransformerParameters(*numbers))
    all_mappers.append(intervals_mapper_factory(current_interval_mappers))
    if seeds is None:
        raise RuntimeError('No seeds found')

    return lambda r: _chain(r, all_mappers), seeds


def _extract_numbers(line: str) -> List[int]:
    return [int(i) for i in re.findall(r'\d+ ?', line)]
