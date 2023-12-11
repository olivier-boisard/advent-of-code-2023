import copy
from dataclasses import dataclass
from typing import Iterable, List

from day05.extraction import extract_map_and_seeds
from day05.mapping import IntervalMapperMixin


def solve(puzzle_input: Iterable[str]) -> int:
    mapper, seed_intervals = extract_map_and_seeds(puzzle_input, _RangeIntervalMapper, _MultipleRangeIntervalMapper)

    interval_starts = seed_intervals[0::2]
    interval_lengths = seed_intervals[1::2]

    intervals = [_FlaggedInterval(start, start + length) for start, length in zip(interval_starts, interval_lengths)]
    intervals = sorted(intervals, key=lambda r: r.start)
    final_intervals = mapper(intervals)

    return final_intervals[0].start


@dataclass
class _FlaggedInterval:
    start: int
    stop: int
    processed: bool

    def __init__(self, start: int, stop: int, processed: bool = False):
        self.start = start
        self.stop = stop
        self.processed = processed


class _RangeIntervalMapper(IntervalMapperMixin):
    def __call__(self, interval: _FlaggedInterval) -> Iterable[_FlaggedInterval]:
        source_interval_stop = self.source_interval_start + self.interval_length - 1
        intervals = []
        shift = self.destination_interval_start - self.source_interval_start
        intervals.append(  # Interval below accepted source interval start
            _FlaggedInterval(
                start=interval.start,
                stop=min(interval.stop, self.source_interval_start)
            )
        )
        intervals.append(  # Interval within accepted source interval bounds
            _FlaggedInterval(
                start=max(interval.start, self.source_interval_start) + shift,
                stop=min(interval.stop, source_interval_stop) + shift,
                processed=True
            )
        )
        intervals.append(  # Interval above accepted source interval end
            _FlaggedInterval(
                start=max(interval.start, source_interval_stop),
                stop=interval.stop
            )
        )

        return filter(lambda i: i.start <= i.stop, intervals)


class _MultipleRangeIntervalMapper:
    def __init__(self, mappers: Iterable[_RangeIntervalMapper]):
        self._mappers = mappers

    def __call__(self, intervals: Iterable[_FlaggedInterval]) -> Iterable[_FlaggedInterval]:
        intervals = copy.deepcopy(intervals)
        for interval in intervals:
            interval.processed = False
        for mapper in self._mappers:
            output_intervals = []
            for interval in intervals:
                if not interval.processed:
                    output_intervals += mapper(interval)
                else:
                    output_intervals.append(interval)
            intervals = output_intervals
        return _unite_intervals(intervals)


def _unite_intervals(intervals: Iterable[_FlaggedInterval]) -> List[_FlaggedInterval]:
    intervals = sorted(intervals, key=lambda r: r.start)
    output = [copy.copy(intervals[0])]
    for current_interval in intervals[1:]:
        last_output_interval = output[-1]
        if last_output_interval.stop >= current_interval.start:
            output[-1] = _FlaggedInterval(start=last_output_interval.start, stop=current_interval.stop)
        else:
            output.append(copy.copy(current_interval))
    return output
