from typing import Iterable

from day08.extraction import extract_network


def solve(puzzle_input: Iterable[str]) -> int:
    puzzle_input = list(puzzle_input)
    instructions = puzzle_input[0]
    network = extract_network(puzzle_input)

    step = 0
    current_nodes = [key for key in network.keys() if key[-1] == 'A']
    while not _stop(current_nodes):
        current_nodes = [network[node][instructions[step % len(instructions)]] for node in current_nodes]
        step += 1
    return step


def _stop(nodes: Iterable[str]) -> bool:
    return all(node[-1] == 'Z' for node in nodes)
