from typing import Iterable

from day02.cubes import CubeSet, extract_games


def solve(puzzle_input: Iterable[str]) -> int:
    is_valid = _GameChecker(
        CubeSet(
            n_red_cubes=12,
            n_green_cubes=13,
            n_blue_cubes=14
        )
    )

    games = extract_games(puzzle_input)
    return sum([game_id for game_id, game in games.items() if is_valid(game)])


class _GameChecker:
    def __init__(self, game_config: CubeSet):
        self._game_config = game_config

    def __call__(self, game: Iterable[CubeSet]):
        game_is_valid = True
        for draw in game:
            if not draw.is_subset_of(self._game_config):
                game_is_valid = False
                break
        return game_is_valid
