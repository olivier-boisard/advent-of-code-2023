from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from typing import Callable


class HandType(IntEnum):
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
    strength_func: Callable[[str], HandType]

    def __int__(self):
        figure_to_int = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        output = 0
        base = max(figure_to_int.values()) + 1
        for i, card in enumerate(self.hand[::-1]):
            output += base ** i * (figure_to_int[card] if card in figure_to_int else int(card))
        return output + self.hand_type * base ** len(self.hand)

    @property
    def hand_type(self) -> HandType:
        return self.strength_func(self.hand)


def standard_strength_computer(hand: str) -> HandType:
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
    return sum(hand.bid * (i + 1) for i, hand in enumerate(sorted(hands, key=int)))
