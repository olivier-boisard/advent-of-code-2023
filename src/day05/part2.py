import copy
from dataclasses import dataclass
from typing import Iterable, Callable

from day05.extraction import extract_map_and_seeds
from day05.range_transformer_parameters import RangeTransformerParameters


def solve(puzzle_input: Iterable[str]) -> int:
    mapper, seed_intervals = extract_map_and_seeds(puzzle_input, _create_mapper)

    interval_starts = seed_intervals[0::2]
    interval_lengths = seed_intervals[1::2]

    intervals = [_Interval(start, start + length) for start, length in zip(interval_starts, interval_lengths)]
    intervals = sorted(intervals, key=lambda r: r.start)
    final_intervals = mapper(intervals)

    return list(final_intervals)[0].start


@dataclass
class _Interval:
    start: int
    stop: int


@dataclass
class _DataWithFlag[T]:
    data: T
    flag: bool


def _create_mapper(
        interval_mapping_parameters: Iterable[RangeTransformerParameters]
) -> Callable[[Iterable[_Interval]], Iterable[_Interval]]:
    transformer = _MultiFlaggedDataTransformer([_SingleIntervalTransformer(p) for p in interval_mapping_parameters])
    return lambda intervals: _unite_intervals(transformer(intervals))


class _SingleIntervalTransformer:

    def __init__(self, parameters: RangeTransformerParameters):
        self._parameters = parameters

    def __call__(self, interval: _Interval) -> Iterable[_DataWithFlag[_Interval]]:
        source_interval_stop = self._parameters.source_interval_start + self._parameters.interval_length - 1
        intervals = []
        shift = self._parameters.destination_interval_start - self._parameters.source_interval_start
        intervals.append(  # Interval below accepted source interval start
            _DataWithFlag(
                data=_Interval(
                    start=interval.start,
                    stop=min(interval.stop, self._parameters.source_interval_start - 1)
                ),
                flag=False
            )
        )
        intervals.append(  # Interval within accepted source interval bounds
            _DataWithFlag(
                data=_Interval(
                    start=max(interval.start, self._parameters.source_interval_start) + shift,
                    stop=min(interval.stop, source_interval_stop) + shift,
                ),
                flag=True
            )
        )
        intervals.append(  # Interval above accepted source interval end
            _DataWithFlag(
                _Interval(
                    start=max(interval.start, source_interval_stop + 1),
                    stop=interval.stop
                ),
                flag=False
            )
        )

        return filter(lambda i: i.data.start <= i.data.stop, intervals)


class _MultiFlaggedDataTransformer[T]:
    def __init__(self, transformers: Iterable[Callable[[T], Iterable[_DataWithFlag[T]]]]):
        self._transformers = transformers

    def __call__(self, data: Iterable[T]) -> Iterable[T]:
        flagged_data_list = [_DataWithFlag(e, flag=False) for e in data]
        for transformer in self._transformers:
            output_data = []
            for flagged_data in flagged_data_list:
                if not flagged_data.flag:
                    output_data += transformer(flagged_data.data)
                else:
                    output_data.append(flagged_data)
            flagged_data_list = output_data
        return [flagged_data.data for flagged_data in flagged_data_list]


def _unite_intervals(intervals: Iterable[_Interval]) -> Iterable[_Interval]:
    intervals = sorted(intervals, key=lambda r: r.start)
    output = [copy.copy(intervals[0])]
    for current_interval in intervals[1:]:
        last_output_interval = output[-1]
        if last_output_interval.stop >= current_interval.start:
            output[-1] = _Interval(start=last_output_interval.start, stop=current_interval.stop)
        else:
            output.append(copy.copy(current_interval))
    return output
