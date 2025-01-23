
#!/usr/bin/python3
""" ItrBFS.py
Student Names:
UW NetIDs:
CSE 415, Winter, 2025, University of Washington

This code contains my implementation of the Iterative BFS algorithm.

Usage:
 python ItrBFS.py HumansRobotsFerry
"""

import sys
import importlib


class ItrBFS:
    """
    Class that implements Iterative BFS for any problem space (provided in the required format)
    """

    def __init__(self, problem):
        """ Initializing the ItrBFS class.
        Please DO NOT modify this method. You may populate the required instance variables
        in the other methods you implement.
        """
        self.Problem = importlib.import_module(problem)
        self.COUNT = None  # Number of nodes expanded
        self.MAX_OPEN_LENGTH = None  # Maximum length of the open list
        self.PATH = None  # Solution path
        self.PATH_LENGTH = None  # Length of the solution path
        self.BACKLINKS = None  # Predecessor links, used to recover the path
        print("\nWelcome to ItrBFS")

    def runBFS(self):
        initial_state = self.Problem.CREATE_INITIAL_STATE()
        self.COUNT = 0
        self.MAX_OPEN_LENGTH = 0
        self.BACKLINKS = {initial_state: None}
        open_list = [initial_state]
        closed_list = []

        while open_list:
            self.MAX_OPEN_LENGTH = max(self.MAX_OPEN_LENGTH, len(open_list))

            current_state = open_list.pop(0)
            closed_list.append(current_state)

            if self.Problem.GOAL_TEST(current_state):
                print(f"Goal reached: {current_state}")
                self.PATH = self.backtrace(current_state)
                self.PATH_LENGTH = len(self.PATH) - 1
                print("Solution path:")
                for state in self.PATH:
                    print(state)
                print(f"Path length: {self.PATH_LENGTH}")
                print(f"Nodes expanded: {self.COUNT}")
                print(f"Max open list length: {self.MAX_OPEN_LENGTH}")
                return

            self.COUNT += 1
            successors = self.Problem.OPERATORS

            for operator in successors:
                if operator.precond(current_state):
                    successor_state = operator.state_transf(current_state)

                    if successor_state not in closed_list and successor_state not in open_list:
                        open_list.append(successor_state)
                        self.BACKLINKS[successor_state] = current_state

        print("No solution found.")
        return

    def backtrace(self, state):
        """
        Backtrack from the goal state to the initial state using backlinks.
        """
        path = []
        while state is not None:
            path.append(state)
            state = self.BACKLINKS[state]
        path.reverse()  # Reverse the path to start from the initial state.
        return [str(s) for s in path]



if __name__ == '__main__':
    if sys.argv == [''] or len(sys.argv) < 2:
        Problem = "TowersOfHanoi"
    else:
        Problem = sys.argv[1]
    BFS = ItrBFS(Problem)
    BFS.runBFS()
