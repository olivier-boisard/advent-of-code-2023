from dataclasses import dataclass
from typing import Iterator


@dataclass
class Point2D:
    line: int
    column: int

    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(line=self.line + other.line, column=self.column + other.column)

    def __iter__(self) -> Iterator[int]:
        for value in [self.line, self.column]:
            yield value

    def is_in_field(self, n_lines: int, n_columns: int):
        return 0 <= self.line < n_lines and 0 <= self.column < n_columns
