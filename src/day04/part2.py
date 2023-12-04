from functools import cache
from typing import Iterable

import tqdm

from day04.card_processing import extract_n_matching_numbers


def solve(puzzle_input: Iterable[str]) -> int:
    cards = [card.split(':')[1] for card in puzzle_input]
    gain_computer = _GainComputer(cards)
    total_cards = len(cards)
    for card_id in tqdm.tqdm(range(len(cards), 0, -1)):
        gain = gain_computer(card_id)
        total_cards += gain
    return total_cards


class _GainComputer:
    def __init__(self, cards: Iterable[str]):
        self._cards = list(cards)

    @cache
    def __call__(self, card_id: int) -> int:
        zero_based_card_id = card_id - 1
        n_winning_numbers = extract_n_matching_numbers(self._cards[zero_based_card_id])
        additional_card_ids = range(card_id + 1, card_id + n_winning_numbers + 1)
        output = len(additional_card_ids)
        for additional_card_id in additional_card_ids:
            output += self(additional_card_id)
        return output
