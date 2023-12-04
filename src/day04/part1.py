from typing import Iterable

from day04.card_processing import extract_n_matching_numbers


def solve(puzzle_input: Iterable[str]) -> int:
    total_value = 0
    for card in puzzle_input:
        numbers = card.split(':')[1]
        n_winning_played_numbers = extract_n_matching_numbers(numbers)
        total_value += 2 ** (n_winning_played_numbers - 1) if n_winning_played_numbers >= 1 else 0
    return total_value
