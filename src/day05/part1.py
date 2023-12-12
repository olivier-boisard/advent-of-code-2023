from typing import Iterable, Callable

from day05.extraction import extract_map_and_seeds
from day05.range_transformer_parameters import RangeTransformerParameters


def solve(puzzle_input: Iterable[str]) -> int:
    mapper, seeds = extract_map_and_seeds(puzzle_input, _create_mapper)
    return min(*[mapper(number) for number in seeds])


def _create_mapper(interval_mapping_parameters: Iterable[RangeTransformerParameters]) -> Callable[[int], int]:
    return _FirstChangeFunctionApplier([_IntegerRangeTransformer(p) for p in interval_mapping_parameters])


class _IntegerRangeTransformer:

    def __init__(self, parameters: RangeTransformerParameters):
        self._parameters = parameters

    def __call__(self, value: int) -> int:
        source_interval_stop = self._parameters.source_interval_start + self._parameters.interval_length
        if self._parameters.source_interval_start <= value < source_interval_stop:
            output = value - self._parameters.source_interval_start + self._parameters.destination_interval_start
        else:
            output = value
        return output


class _FirstChangeFunctionApplier[T]:
    def __init__(self, funcs: Iterable[Callable[[T], T]]):
        self._funcs = funcs

    def __call__(self, key: T) -> T:
        output = key
        for mapper in self._funcs:
            output = mapper(key)
            if key != output:
                break
        return output
