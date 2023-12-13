from collections import Counter
from typing import Iterable

from day07.hand import HandType, standard_type_extractor, HandStrengthComputer
from day07.game import run


def solve(puzzle_input: Iterable[str]) -> int:
    figure_to_int = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    return run(puzzle_input, HandStrengthComputer(figure_to_int, _with_joker_type_extractor))


def _with_joker_type_extractor(hand: str) -> HandType:
    joker_str = 'J'
    n_most_common_cards = 2

    most_common_cards = Counter(hand.replace(joker_str, '')).most_common(n_most_common_cards)
    replacement_card = most_common_cards[0][0] if len(most_common_cards) > 0 else 'A'
    return standard_type_extractor(hand.replace(joker_str, replacement_card))
