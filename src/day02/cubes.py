import dataclasses
from typing import Iterable, Mapping


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


def extract_games(games: Iterable[str]) -> Mapping[int, Iterable[CubeSet]]:
    output = {}
    for line in games:
        game_str = line.split(': ')
        game_id = int(game_str[0].split(' ')[-1])

        game = _extract_game(game_str[1])
        output[game_id] = game
    return output


def _extract_game(game_str: str) -> Iterable[CubeSet]:
    game = []
    draws_str = game_str.split('; ')
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
    return game
