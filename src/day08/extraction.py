import re
from typing import Iterable, Mapping


def extract_network(puzzle_input: Iterable[str]) -> Mapping[str, Mapping[str, str]]:
    network = {}
    for line in puzzle_input[2:]:
        nodes = re.findall(r'([0-9A-Z]+)', line)
        network[nodes[0]] = {'L': nodes[1], 'R': nodes[2]}
    return network
