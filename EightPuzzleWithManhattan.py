"""EightPuzzleWithManhattan.py
This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is the Manhattan distance, which sums
the distances of the tiles from their goal positions.

"""

from EightPuzzle import *

def h(s):
    """Return an estimate of the sum of the distances of the tiles
    from their goal positions compared to the goal state."""

    goal_positions = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2)
    }
    manhattan_distance = 0

    for i in range(3):
        for j in range(3):
            tile = s.b[i][j]
            if tile != 0:
                goal_i, goal_j = goal_positions[tile]
                manhattan_distance += abs(i - goal_i) + abs(j - goal_j)

    return manhattan_distance