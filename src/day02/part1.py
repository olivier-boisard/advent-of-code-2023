import dataclasses
from typing import Iterable


@dataclasses.dataclass
class CubeSet:
    n_blue_cubes: int
    n_red_cubes: int
    n_green_cubes: int

    def is_subset_of(self, other: 'CubeSet') -> bool:
        enough_blue_cubes = other.n_blue_cubes >= self.n_blue_cubes
        enough_red_cubes = other.n_red_cubes >= self.n_red_cubes
        enough_green = other.n_green_cubes >= self.n_green_cubes
        return enough_blue_cubes and enough_red_cubes and enough_green


def solve(puzzle_input: Iterable[str]) -> int:
    game_config = CubeSet(
        n_red_cubes=12,
        n_green_cubes=13,
        n_blue_cubes=14
    )

    games = {}
    for line in puzzle_input:
        game_str = line.split(': ')
        game_id = int(game_str[0].split(' ')[-1])
        game = []

        draws_str = game_str[1].split('; ')
        for draw_str in draws_str:
            color_map = {}
            for color_str in draw_str.split(', '):
                color_str_split = color_str.split(' ')
                color_map[color_str_split[1]] = int(color_str_split[0])
            game.append(
                CubeSet(
                    n_blue_cubes=color_map.get('blue', 0),
                    n_red_cubes=color_map.get('red', 0),
                    n_green_cubes=color_map.get('green', 0)
                )
            )
        games[game_id] = game

    valid_game_ids = []
    for game_id, draws in games.items():
        game_is_valid = True
        for draw in draws:
            if not draw.is_subset_of(game_config):
                game_is_valid = False
                break
        if game_is_valid:
            valid_game_ids.append(game_id)

    return sum(valid_game_ids)
