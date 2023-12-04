import copy
import itertools
from typing import Iterable

from day03.extraction import extract_symbols, extract_parts
from day03.part import Point2D, Part


def solve(puzzle_input: Iterable[str]) -> int:
    puzzle_input = list(puzzle_input)
    parts = extract_parts(puzzle_input)
    parts_filter = _PartsFilter(extract_symbols(puzzle_input))
    return sum(part.number for part in parts_filter(parts))


class _PartsFilter:

    def __init__(self, symbols=Iterable[Point2D]):
        self._symbols = symbols

    def __call__(self, parts: Iterable[Part]) -> Iterable[Part]:
        parts = list(parts)
        selected_parts = []
        for symbol in self._symbols:
            remaining_parts = copy.copy(parts)
            for part in remaining_parts:
                for neighbor_relative_coordinates in itertools.product(*[range(-1, 2)] * 2):
                    point = symbol + Point2D(*neighbor_relative_coordinates)
                    if part.covers(point):
                        parts.remove(part)
                        selected_parts.append(part)
                        break
        return selected_parts
