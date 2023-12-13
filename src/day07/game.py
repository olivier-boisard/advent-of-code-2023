from typing import Callable, Iterable


def run(puzzle_input: Iterable[str], hand_strength_computer: Callable[[str], int]) -> int:
    puzzle_input = list(puzzle_input)
    hands = [line.split(' ')[0] for line in puzzle_input]
    bids = [int(line.split(' ')[1]) for line in puzzle_input]
    index = list(range(len(hands)))

    sorted_index = sorted(index, key=lambda i: hand_strength_computer(hands[i]))
    return sum([(i + 1) * bids[index] for i, index in enumerate(sorted_index)])
