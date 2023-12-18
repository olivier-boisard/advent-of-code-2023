from typing import Iterable
import numpy as np


def solve(puzzle_input: Iterable[str]) -> int:
    histories = [np.array(line.split(' '), dtype=int) for line in puzzle_input]
    predicted_value = []
    for history in histories:
        diff = np.diff(history)
        last_elements = [history[-1]]
        while not np.all(diff == 0):
            last_elements.append(diff[-1])
            diff = np.diff(diff)
        predicted_value.append(np.sum(last_elements))
    return np.sum(predicted_value)
