from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from typing import Iterable


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

    def __int__(self):
        digit_mapping = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        max_digit_value = max(digit_mapping.values())
        output = 0
        for i, card in enumerate(self.hand[::-1]):
            output += max_digit_value ** i * (digit_mapping[card] if card in digit_mapping else int(card))
        return output + self.strength * max_digit_value ** (len(self.hand) + 1)

    @property
    def strength(self) -> Strength:
        highest_occurrences_count = max(Counter(self.hand).values())
        if self.n_different_cards == 1:
            output = Strength.FIVE_OF_A_KIND
        elif self.n_different_cards == 2:
            output = Strength.FOUR_OF_A_KIND if highest_occurrences_count == 4 else Strength.FULL_HOUSE
        elif self.n_different_cards == 3:
            output = Strength.THREE_OF_A_KIND if highest_occurrences_count == 3 else Strength.TWO_PAIRS
        elif self.n_different_cards == 4:
            output = Strength.ONE_PAIR
        else:
            output = Strength.HIGH_CARD
        return output

    @property
    def n_different_cards(self) -> int:
        return len(set(self.hand))


def solve(puzzle_input: Iterable[str]) -> int:
    hands = []
    for line in puzzle_input:
        parts = line.split(' ')
        hands.append(
            HandWithBid(
                hand=parts[0],
                bid=int(parts[1])
            )
        )
    hands = sorted(hands, key=lambda h: int(h))
    return sum(hand.bid * (i + 1) for i, hand in enumerate(hands))
