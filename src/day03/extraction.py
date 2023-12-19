import re
from typing import Iterable

from day03.part import Part
from point2d import Point2D


def extract_symbols(puzzle_input: Iterable[str]) -> Iterable:
    symbols = []
    for line_number, line in enumerate(puzzle_input):
        for column_number, character in enumerate(line):
            if not character.isdecimal() and character != '.':
                symbols.append(Point2D(line_number, column_number))
    return symbols


def extract_parts(puzzle_input):
    parts = []
    for line_number, line in enumerate(puzzle_input):
        parts_id = [int(s) for s in re.findall(r'\d*', line) if s.isnumeric()]
        part_starts = [m.start(0) for m in re.finditer(r'(\d+)\.*', line)]
        for part, part_start in zip(parts_id, part_starts):
            parts.append(Part(part, Point2D(line_number, part_start)))
    return parts
