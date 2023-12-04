from dataclasses import dataclass
from math import ceil, log10


@dataclass
class Point2D:
    line: int

    column: int

    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(line=self.line + other.line, column=self.column + other.column)


@dataclass
class Part:
    number: int
    location: Point2D

    def __len__(self) -> int:
        return int(ceil(log10(self.number)))

    def covers(self, location: Point2D) -> bool:
        same_line = location.line == self.location.line
        covered_by_column = self.location.column <= location.column < self.location.column + len(self)
        return same_line and covered_by_column
