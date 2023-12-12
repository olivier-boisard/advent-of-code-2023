from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from typing import Callable

FIGURE_TO_INT = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
INT_TO_FIGURE = {value: key for key, value in FIGURE_TO_INT.items()}


class Strength(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


@dataclass
class HandWithBid:
    hand: str
    bid: int
    strength_func: Callable[[str], Strength]

    def __int__(self):
        max_digit_value = max(FIGURE_TO_INT.values())
        output = 0
        for i, card in enumerate(self.hand[::-1]):
            output += max_digit_value ** i * (FIGURE_TO_INT[card] if card in FIGURE_TO_INT else int(card))
        return output + self.strength * max_digit_value ** (len(self.hand) + 1)

    @property
    def strength(self) -> Strength:
        return self.strength_func(self.hand)


def standard_strength_computer(hand: str) -> Strength:
    highest_occurrences_count = max(Counter(hand).values())
    n_different_cards = len(set(hand))
    if n_different_cards == 1:
        output = Strength.FIVE_OF_A_KIND
    elif n_different_cards == 2:
        output = Strength.FOUR_OF_A_KIND if highest_occurrences_count == 4 else Strength.FULL_HOUSE
    elif n_different_cards == 3:
        output = Strength.THREE_OF_A_KIND if highest_occurrences_count == 3 else Strength.TWO_PAIRS
    elif n_different_cards == 4:
        output = Strength.ONE_PAIR
    else:
        output = Strength.HIGH_CARD
    return output


def run_game(puzzle_input, strength_func):
    hands = []
    for line in puzzle_input:
        parts = line.split(' ')
        hands.append(
            HandWithBid(
                hand=parts[0],
                bid=int(parts[1]),
                strength_func=strength_func
            )
        )
    hands = sorted(hands, key=lambda h: int(h))
    return sum(hand.bid * (i + 1) for i, hand in enumerate(hands))
