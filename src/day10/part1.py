import sys
from enum import Enum
from typing import Iterable, Tuple

import numpy as np


class DirectionConfig:
    def __init__(self, compatible_pipes: str, relative_coordinates: Tuple[int, int]):
        self._compatible_pipes = compatible_pipes
        self._relative_coordinates = relative_coordinates

    @property
    def relative_coordinates(self):
        return self._relative_coordinates

    def pipe_is_compatible(self, pipe: str) -> bool:
        return pipe in self._compatible_pipes


class DirectionEnum(Enum):
    NORTH = DirectionConfig(compatible_pipes='|7F', relative_coordinates=(-1, 0))
    EAST = DirectionConfig(compatible_pipes='-J7', relative_coordinates=(0, 1))
    SOUTH = DirectionConfig(compatible_pipes='|LJ', relative_coordinates=(1, 0))
    WEST = DirectionConfig(compatible_pipes='-FL', relative_coordinates=(0, -1))


def solve(puzzle_input: Iterable[str]) -> int:
    field = np.array([list(line) for line in puzzle_input], dtype=str)
    current_position = tuple(np.argwhere(field == 'S')[0])
    visited_nodes = np.zeros_like(field, dtype=bool)
    cost_matrix = sys.maxsize * np.ones_like(field, dtype=int)
    cost_matrix[current_position] = 0

    # Run Dijkstra
    min_non_visited_cost = cost_matrix[~visited_nodes].min()
    while not visited_nodes.all() and min_non_visited_cost != sys.maxsize:
        current_position = tuple(np.argwhere((cost_matrix == min_non_visited_cost) & ~visited_nodes)[0])
        for direction in DirectionEnum:
            rx, ry = direction.value.relative_coordinates
            x = current_position[0].item() + rx
            y = current_position[1].item() + ry

            x_is_out_of_bound = x < 0 or x >= field.shape[0]
            y_is_out_of_bound = y < 0 or y >= field.shape[1]
            if x_is_out_of_bound or y_is_out_of_bound:
                continue

            if direction.value.pipe_is_compatible(str(field[x, y])):
                cost_matrix[x, y] = min(cost_matrix[x, y], cost_matrix[current_position] + 1)
        visited_nodes[current_position] = True
        min_non_visited_cost = cost_matrix[~visited_nodes].min()

    # Find most distant point in loop
    return cost_matrix[cost_matrix != sys.maxsize].max()
