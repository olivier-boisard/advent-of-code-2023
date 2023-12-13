from collections import Counter
from typing import Iterable, Tuple, List

from day07.hand import HandType, standard_strength_computer, run_game, FIGURE_TO_INT, INT_TO_FIGURE


def solve(puzzle_input: Iterable[str]) -> int:
    return run_game(puzzle_input, _joker_strength_computer)


def _joker_strength_computer(hand: str) -> HandType:
    jocker_str = 'J'
    n_most_common_cards = 2
    hand_without_jokers = hand.replace(jocker_str, '')
    most_common_cards = Counter(hand_without_jokers).most_common(n_most_common_cards)
    if len(most_common_cards) == 0:  # if there are only jokers in the hand
        replacement_card = 'A'
    else:
        most_common_card_count = most_common_cards[0]
        replacement_card = most_common_card_count[0]
        if most_common_card_count[1] == 1:  # if each card is different
            replacement_card = _extract_most_powerful_card(hand_without_jokers)
        else:
            if len(most_common_cards) == n_most_common_cards:
                if most_common_card_count[1] == 2 and most_common_cards[1][1] == 2:  # if there are two pairs
                    replacement_card = _extract_highest_pair_card(most_common_cards)
    return standard_strength_computer(hand.replace(jocker_str, replacement_card))


def _extract_highest_pair_card(most_common_cards: List[Tuple[str, int]]) -> str:
    most_common_card = most_common_cards[0][0]
    second_most_common_card = most_common_cards[1][0]
    highest_pair_value = max(_compute_card_value(most_common_card), _compute_card_value(second_most_common_card))
    return INT_TO_FIGURE[highest_pair_value] if highest_pair_value in INT_TO_FIGURE else str(highest_pair_value)


def _compute_card_value(card: str) -> int:
    return FIGURE_TO_INT[card] if card in FIGURE_TO_INT else int(card)


def _extract_most_powerful_card(hand_without_jokers):
    card_values = []
    for card in hand_without_jokers:
        card_values.append(FIGURE_TO_INT[card] if card in FIGURE_TO_INT else int(card))
    max_card_value = max(card_values)
    return INT_TO_FIGURE[max_card_value] if max_card_value in INT_TO_FIGURE else str(max_card_value)
