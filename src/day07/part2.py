from collections import Counter
from typing import Iterable

from day07.hand import HandType, standard_strength_computer, run_game


def solve(puzzle_input: Iterable[str]) -> int:
    return run_game(puzzle_input, _joker_strength_computer)


def _joker_strength_computer(hand: str) -> HandType:
    jocker_str = 'J'
    n_most_common_cards = 2
    hand_without_jokers = hand.replace(jocker_str, '')
    most_common_cards = Counter(hand_without_jokers).most_common(n_most_common_cards)
    replacement_card = most_common_cards[0][0] if len(most_common_cards) > 0 else 'A'
    return standard_strength_computer(hand.replace(jocker_str, replacement_card))
