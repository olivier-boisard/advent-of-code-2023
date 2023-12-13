from collections import Counter
from enum import IntEnum
from typing import Mapping, Callable


class HandType(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


def standard_type_extractor(hand: str) -> HandType:
    highest_occurrences_count = max(Counter(hand).values())
    n_different_cards = len(set(hand))
    if n_different_cards == 1:
        output = HandType.FIVE_OF_A_KIND
    elif n_different_cards == 2:
        output = HandType.FOUR_OF_A_KIND if highest_occurrences_count == 4 else HandType.FULL_HOUSE
    elif n_different_cards == 3:
        output = HandType.THREE_OF_A_KIND if highest_occurrences_count == 3 else HandType.TWO_PAIRS
    elif n_different_cards == 4:
        output = HandType.ONE_PAIR
    else:
        output = HandType.HIGH_CARD
    return output


class HandStrengthComputer:
    def __init__(
            self,
            figure_to_int: Mapping[str, int],
            type_extractor: Callable[[str], int] = standard_type_extractor
    ):
        self._figure_to_int = figure_to_int
        self._type_extractor = type_extractor

    def __call__(self, hand: str) -> int:
        output = 0
        base = max(self._figure_to_int.values()) + 1
        for i, card in enumerate(hand[::-1]):
            output += base ** i * (self._figure_to_int[card] if card in self._figure_to_int else int(card))
        return output + self._type_extractor(hand) * base ** len(hand)
