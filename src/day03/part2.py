import itertools
from typing import Iterable

from day03.extraction import extract_parts, extract_symbols
from day03.part import Point2D, Part


def solve(puzzle_input: Iterable[str]) -> int:
    puzzle_input = list(puzzle_input)
    parts = extract_parts(puzzle_input)
    return _TotalGearRatioComputer(extract_symbols(puzzle_input))(parts)


class _TotalGearRatioComputer:

    def __init__(self, symbols=Iterable[Point2D]):
        self._symbols = symbols

    def __call__(self, parts: Iterable[Part]) -> int:
        parts = list(parts)
        parts_per_gear = 2
        total_gear_ratio = 0
        for symbol in self._symbols:
            adjacent_parts = self._extract_adjacent_part(parts, symbol)
            if len(adjacent_parts) == parts_per_gear:
                gear_ratio = 1
                for part in adjacent_parts:
                    gear_ratio *= part.number
                total_gear_ratio += gear_ratio
        return total_gear_ratio

    @staticmethod
    def _extract_adjacent_part(parts, symbol):
        adjacent_parts = []
        for part in parts:
            for neighbor_relative_coordinates in itertools.product(*[range(-1, 2)] * 2):
                point = symbol + Point2D(*neighbor_relative_coordinates)
                if part.covers(point) and part not in adjacent_parts:
                    adjacent_parts.append(part)
        return adjacent_parts
