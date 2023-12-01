import importlib
import sys

import typer
from puzzle_solver import PuzzleSolver

app = typer.Typer()


@app.command()
def solve(solver_plugin_name: str, input_file_path: str, expected_output: int = None):
    # Load dynamic dependencies
    solver_module = importlib.import_module(solver_plugin_name)

    # Set up application
    puzzle_solver = PuzzleSolver(solver_module.solve)

    # Run application
    output = puzzle_solver(input_file_path)
    if expected_output is not None:
        if output != expected_output:
            sys.stderr.write(f"{output} is different than the expected output ({expected_output})\n")
            print(sys.exit(-1))
    else:
        print(output)


if __name__ == "__main__":
    app()
