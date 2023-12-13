from typing import Iterable, List

from day08.extraction import extract_network


class TargetStepFinder:
    def __init__(self, target_nodes_steps: List[int], loop_index: int):
        self._target_nodes_steps = target_nodes_steps
        self._loop_index = loop_index
        self._current_position = None
        self._n_calls = 0

    def move_to_next_target(self):
        if self._n_calls < len(self._target_nodes_steps):
            new_position = self._target_nodes_steps[self._n_calls]
        else:
            target_nodes_steps_within_loop = [step for step in self._target_nodes_steps if step >= self._loop_index]
            shift = len(self._target_nodes_steps) - len(target_nodes_steps_within_loop)
            position_in_loop = (self._n_calls - shift) % len(target_nodes_steps_within_loop)
            n_loops = (self._n_calls - shift) // len(target_nodes_steps_within_loop)
            new_position = target_nodes_steps_within_loop[position_in_loop] + n_loops * self._target_nodes_steps[-1]
        self._n_calls += 1
        self._current_position = new_position

    @property
    def current_step(self) -> int:
        return self._current_position


def solve(puzzle_input: Iterable[str]) -> int:
    puzzle_input = list(puzzle_input)
    instructions = puzzle_input[0]
    network = extract_network(puzzle_input)
    starting_nodes = [key for key in network.keys() if key[-1] == 'A']
    target_steps_finders = []
    for starting_node in starting_nodes:
        path = []
        current_node = starting_node
        current_instruction = instructions[0]
        step = 0
        loop_index = None
        while loop_index is None:
            step += 1
            path.append(current_node)
            current_node = network[current_node][current_instruction]
            current_instruction = instructions[step % len(instructions)]

            visited_node_steps = [i for i, node in enumerate(path) if node == current_node]
            for visited_node_step in visited_node_steps:
                if (step % len(instructions)) == visited_node_step:
                    loop_index = visited_node_step
                    break
        target_nodes_steps = [i for i, node in enumerate(path) if node[-1] == 'Z']
        target_steps_finders.append(TargetStepFinder(target_nodes_steps, loop_index))

    for finder in target_steps_finders:
        finder.move_to_next_target()
    while not _stop(target_steps_finders):
        min_step = min(finder.current_step for finder in target_steps_finders)
        for finder in target_steps_finders:
            if finder.current_step == min_step:
                finder.move_to_next_target()

    return target_steps_finders[0].current_step


def _stop(target_steps_finders: List[TargetStepFinder]) -> bool:
    output = True
    for finder in target_steps_finders[1:]:
        if finder.current_step != target_steps_finders[0].current_step:
            output = False
            break
    return output
