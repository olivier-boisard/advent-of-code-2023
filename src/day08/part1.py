from typing import Iterable

from day08.extraction import extract_network


def solve(puzzle_input: Iterable[str]) -> int:
    puzzle_input = list(puzzle_input)
    instructions = puzzle_input[0]
    network = extract_network(puzzle_input)

    step = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        current_node = network[current_node][instructions[step % len(instructions)]]
        step += 1
    return step
