from collections import Counter
from typing import Iterable

from day07.hand import Strength, standard_strength_computer, run_game, FIGURE_TO_INT, INT_TO_FIGURE


def solve(puzzle_input: Iterable[str]) -> int:
    return run_game(puzzle_input, _jocker_strength_computer)


def _jocker_strength_computer(hand: str) -> Strength:
    jocker_str = 'J'
    n_most_common_cards = 2
    hand_without_jokers = hand.replace(jocker_str, '')
    most_common_cards = Counter(hand_without_jokers).most_common(n_most_common_cards)
    if len(most_common_cards) == 0:  # if there are only jokers in the hand
        replacement_card = 'A'
    else:
        most_common_card_count = most_common_cards[0]
        most_common_card = most_common_card_count[0]
        replacement_card = most_common_card
        if most_common_card_count[1] == 1:  # if each card is different
            card_values = []
            for card in hand_without_jokers:
                card_values.append(FIGURE_TO_INT[card] if card in FIGURE_TO_INT else int(card))
            max_card_value = max(card_values)
            replacement_card = INT_TO_FIGURE[max_card_value] if max_card_value in INT_TO_FIGURE else str(max_card_value)
        else:
            if len(most_common_cards) == n_most_common_cards:
                second_most_common_card_count = most_common_cards[1]
                if most_common_card_count[1] == 2 and second_most_common_card_count[1] == 2:  # if there are two pairs
                    second_most_common_card = second_most_common_card_count[0]
                    highest_pair_value = max(
                        FIGURE_TO_INT[most_common_card] if most_common_card in FIGURE_TO_INT else int(most_common_card),
                        FIGURE_TO_INT[second_most_common_card] if second_most_common_card in FIGURE_TO_INT else int(second_most_common_card)
                    )
                    replacement_card = INT_TO_FIGURE[highest_pair_value] if highest_pair_value in INT_TO_FIGURE else str(highest_pair_value)
    hand = hand.replace(jocker_str, replacement_card)

    return standard_strength_computer(hand)
