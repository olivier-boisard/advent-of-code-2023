from typing import Iterable

from day02.cubes import extract_games


def solve(puzzle_input: Iterable[str]) -> int:
    return sum(_compute_game_power(game) for game in extract_games(puzzle_input).values())


def _compute_game_power(game):
    min_blue_cubes = 0
    min_red_cubes = 0
    min_green_cubes = 0
    for draw in game:
        min_blue_cubes = max(min_blue_cubes, draw.n_blue_cubes)
        min_red_cubes = max(min_red_cubes, draw.n_red_cubes)
        min_green_cubes = max(min_green_cubes, draw.n_green_cubes)
    return min_blue_cubes * min_red_cubes * min_green_cubes
