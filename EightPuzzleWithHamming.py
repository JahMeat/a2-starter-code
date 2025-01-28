"""EightPuzzleWithHamming.py
This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is the Hamming distance, which counts
the number of tiles out of place.

"""

from EightPuzzle import *

def h(s):
    """Return an estimate of the number of tiles out of place
    compared to the goal state."""

    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    hamming_distance = 0

    for i in range(3):
        for j in range(3):
            if s.b[i][j] != 0 and s.b[i][j] != goal_state[i][j]:
                hamming_distance += 1

    return hamming_distance