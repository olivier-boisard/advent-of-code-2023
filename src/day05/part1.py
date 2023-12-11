from typing import Iterable

from day05.extraction import extract_map_and_seeds
from day05.mapping import IntervalMapperMixin


def solve(puzzle_input: Iterable[str]) -> int:
    mapper, seeds = extract_map_and_seeds(puzzle_input, _IntegerIntervalMapper, _MultipleIntegerIntervalMapper)
    return min(*[mapper(number) for number in seeds])


class _IntegerIntervalMapper(IntervalMapperMixin):

    def __init__(self, *args):
        super().__init__(*args)

    def __call__(self, value: int) -> int:
        if self.source_interval_start <= value < self.source_interval_start + self.interval_length:
            output = value - self.source_interval_start + self.destination_interval_start
        else:
            output = value
        return output


class _MultipleIntegerIntervalMapper:
    def __init__(self, mappers: Iterable[_IntegerIntervalMapper]):
        self._mappers = mappers

    def __call__(self, key: int) -> int:
        output = key
        for mapper in self._mappers:
            output = mapper(key)
            if key != output:
                break
        return output
