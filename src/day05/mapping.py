import copy
from dataclasses import dataclass
from typing import Iterable, Callable, List
from multimethod import multimethod


@dataclass
class Interval:
    start: int
    stop: int


def _unite_intervals(intervals: Iterable[Interval]) -> List[Interval]:
    intervals = sorted(intervals, key=lambda r: r.start)
    output = [copy.copy(intervals[0])]
    for current_interval in intervals[1:]:
        last_output_interval = output[-1]
        if last_output_interval.stop >= current_interval.start:
            output[-1] = Interval(start=last_output_interval.start, stop=current_interval.stop)
        else:
            output.append(copy.copy(current_interval))
    return output


class IntervalMapper:
    def __init__(
            self,
            destination_interval_start: int,
            source_interval_start: int,
            interval_length: int
    ):
        self._destination_interval_start = destination_interval_start
        self._source_interval_start = source_interval_start
        self._interval_length = interval_length

    @multimethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError(f'Cannot process inputs: {args}, {kwargs}')

    @__call__.register
    def _(self, value: int) -> int:
        if self._source_interval_start <= value < self._source_interval_start + self._interval_length:
            output = value - self._source_interval_start + self._destination_interval_start
        else:
            output = value
        return output

    @__call__.register
    def _(self, input_intervals: Iterable[Interval]) -> Iterable[Interval]:
        source_interval_stop = self._source_interval_start + self._interval_length - 1
        intervals = []
        shift = self._destination_interval_start - self._source_interval_start
        for input_interval in input_intervals:
            intervals.append(  # Interval below accepted source interval start
                Interval(
                    start=input_interval.start,
                    stop=min(input_interval.stop, self._source_interval_start)
                )
            )
            intervals.append(  # Interval within accepted source interval bounds
                Interval(
                    start=max(input_interval.start, self._source_interval_start) + shift,
                    stop=min(input_interval.stop, source_interval_stop) + shift
                )
            )
            intervals.append(  # Interval above accepted source interval end
                Interval(
                    start=max(input_interval.start, source_interval_stop),
                    stop=input_interval.stop
                )
            )

        return _unite_intervals(filter(lambda interval: interval.start <= interval.stop, intervals))


class MultipleMapper[T]:
    def __init__(self, mappers: Iterable[Callable[[T], T]]):
        self._mappers = mappers

    def __call__(self, item: T) -> T:
        output = item
        for mapper in self._mappers:
            output = mapper(item)
            if output != item:
                break
        return output
