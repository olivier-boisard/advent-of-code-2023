from typing import Iterable, Tuple, cast

import numpy as np

from point2d import Point2D


def solve(puzzle_input: Iterable[str]) -> int:
    field = np.array([list(line) for line in puzzle_input], dtype=str)
    current_position = Point2D(*np.argwhere(field == 'S')[0])
    visited_nodes = np.zeros_like(field, dtype=bool)
    visited_nodes[*current_position] = True
    pipes = []

    # Build polygon
    polygon = []
    stop = False
    while not stop:
        polygon.append(current_position)
        visited_nodes[*current_position] = True
        current_pipe = field[*current_position]
        pipes.append(current_pipe)
        north = Point2D(-1, 0)
        south = Point2D(1, 0)
        west = Point2D(0, -1)
        east = Point2D(0, 1)
        if current_pipe == 'S':
            relative_points_to_connecting_pipes = [
                (north, '|7F'),
                (south, '|JL'),
                (west, 'F-L'),
                (east, '-J7'),
            ]
            for r, connecting_pipes in relative_points_to_connecting_pipes:
                p = current_position + r
                if not p.is_in_field(*field.shape):
                    continue
                if field[*p] in connecting_pipes:
                    current_position = p
                    break
        else:
            pipe_to_potential_next_relative_positions = {
                '-': (east, west),
                '|': (north, south),
                'F': (south, east),
                '7': (south, west),
                'L': (north, east),
                'J': (north, west)
            }
            stop = True
            for potential_next_relative_position in pipe_to_potential_next_relative_positions[current_pipe]:
                potential_next_position = potential_next_relative_position + current_position
                if not potential_next_position.is_in_field(*field.shape):
                    continue
                if not visited_nodes[*potential_next_position]:
                    current_position = potential_next_position
                    stop = False
                    break

    polygon = np.array([tuple(node) for node in polygon])
    assert _polygon_is_valid(cast(Iterable[Tuple[int, int]], polygon))

    area_part_1 = polygon[:, 0] * np.roll(polygon[:, 1], -1)
    area_part_2 = np.roll(polygon[:, 0], -1) * polygon[:, 1]
    area = np.abs((area_part_1 - area_part_2).sum()) // 2

    n_corners = _extract_n_corner_pipes(pipes)
    n_edges = len(polygon) - n_corners

    return area - (n_corners - 4) // 2 - n_edges // 2 - 1


def _polygon_is_valid(polygon: Iterable[Tuple[int, int]]) -> bool:
    polygon = list(polygon)
    vertex = polygon.pop(0)
    polygon.append(vertex)
    output = True
    for i, next_vertex in enumerate(polygon):
        distance = abs(vertex[0] - next_vertex[0]) + abs(vertex[1] - next_vertex[1])
        if distance != 1:
            output = False
            break
        vertex = next_vertex
    return output


def _extract_n_corner_pipes(pipes: Iterable[str]) -> int:
    n_corners = sum([pipe in 'JF7L' for pipe in pipes])
    if n_corners % 2 != 0:
        n_corners += 1
    return n_corners
