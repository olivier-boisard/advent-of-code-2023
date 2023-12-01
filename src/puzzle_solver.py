from typing import Callable, Iterable, Iterator


class PuzzleSolver:
    def __init__(self, solve_func: Callable[[Iterable[str]], int]):
        self._solve_func = solve_func

    def __call__(self, input_file_path: str) -> int:
        puzzle_input = PuzzleSolver._load_puzzle_input(input_file_path)
        return self._solve_func(puzzle_input)

    @staticmethod
    def _load_puzzle_input(input_file_path: str) -> Iterator[str]:
        with open(input_file_path) as f:
            for line in f.readlines():
                yield line.strip()
