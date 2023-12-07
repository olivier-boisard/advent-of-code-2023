from typing import Iterable, Callable


class RangeMapper:
    destination_range_start: int
    source_range_start: int
    range_length: int

    def __init__(
            self,
            destination_range_start: int,
            source_range_start: int,
            range_length: int
    ):
        self._destination_range_start = destination_range_start
        self._source_range_start = source_range_start
        self._range_length = range_length

    def __call__(self, value: int) -> int:
        if self._source_range_start <= value < self._source_range_start + self._range_length:
            output = value - self._source_range_start + self._destination_range_start
        else:
            output = value
        return output


class MultipleMapper[T, U]:
    def __init__(self, mappers: Iterable[Callable[[T], U]]):
        self._mappers = mappers

    def __call__(self, item: T) -> U:
        output = item
        for mapper in self._mappers:
            output = mapper(item)
            if output != item:
                break
        return output
