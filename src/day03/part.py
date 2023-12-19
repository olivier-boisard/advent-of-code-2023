from dataclasses import dataclass
from math import ceil, log10

from point2d import Point2D


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
