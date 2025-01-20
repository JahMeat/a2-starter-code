'''Farmer_Fox.py
[STUDENTS: REPLACE THE FOLLOWING INFORMATION WITH YOUR
OWN:]
by Jah Chen and Eugene Cheung
UWNetIDs: jah0311, ...
Student numbers: 2235225, ...

Assignment 2, in CSE 415, Winter 2025
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name(s), uwnetid(s), and 7-digit student number(s) are given above in 
# the format shown.

# You should model your code closely after the given example problem
# formulation in HumansRobotsFerry.py

# Put your metadata here, in the same format as in HumansRobotsFerry.

# Start your Common Code section here.

class State:

    # include methods similar to those in HumansRobotsFerry.py for
    # this class.
    def __init__(self, old=None):
        if old is None:
            self.farmer = 'left'
            self.fox = 'left'
            self.chicken = 'left'
            self.grain = 'left'
        else:
            self.farmer = old.farmer
            self.fox = old.fox
            self.chicken = old.chicken
            self.grain = old.grain

        

# Put your INITIAL STATE section here.

# Put your OPERATORS section here.

class Operator:
    pass

# etc.


# Finish off with the GOAL_TEST and GOAL_MESSAGE_FUNCTION here.

