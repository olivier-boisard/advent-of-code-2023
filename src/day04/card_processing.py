from typing import Iterable


def extract_numbers(numbers: str) -> Iterable[int]:
    return [int(number) for number in numbers.split(' ') if number.isnumeric()]


def extract_n_matching_numbers(card_numbers: str) -> int:
    number_parts = card_numbers.split('|')
    winning_numbers = extract_numbers(number_parts[0])
    played_numbers = extract_numbers(number_parts[1])
    winning_played_numbers = [played_number for played_number in played_numbers if played_number in winning_numbers]
    return len(winning_played_numbers)
