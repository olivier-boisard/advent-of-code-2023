from typing import Iterable

from day02.cubes import CubeSet, GameChecker, extract_games


def solve(puzzle_input: Iterable[str]) -> int:
    is_valid = GameChecker(
        CubeSet(
            n_red_cubes=12,
            n_green_cubes=13,
            n_blue_cubes=14
        )
    )

    games = extract_games(puzzle_input)
    return sum([game_id for game_id, game in games.items() if is_valid(game)])


