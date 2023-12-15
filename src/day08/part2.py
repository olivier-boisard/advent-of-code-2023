import math
from typing import Iterable

from day08.extraction import extract_network


def solve(puzzle_input: Iterable[str]) -> int:
    puzzle_input = list(puzzle_input)
    instructions = puzzle_input[0]
    network = extract_network(puzzle_input)
    starting_nodes = [key for key in network.keys() if key[-1] == 'A']
    steps = []
    for starting_node in starting_nodes:
        current_node = starting_node
        step = 0
        while current_node[-1] != 'Z':
            current_node = network[current_node][instructions[step % len(instructions)]]
            step += 1
        steps.append(step)
    return math.lcm(*steps)
