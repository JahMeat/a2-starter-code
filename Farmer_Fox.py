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
PROBLEM_NAME = "Farmer, Fox, Chicken, and Grain"
PROBLEM_VERSION = "1.1"
PROBLEM_AUTHORS = ['S. Tanimoto']
PROBLEM_CREATION_DATE = "10-JAN-2025"
# Start your Common Code section here.
Bank = ['farmer', 'fox', 'chicken', 'grain']
LEFT = 0
RIGHT = 1

class State:

    # include methods similar to those in HumansRobotsFerry.py for
    # this class.
    def __init__(self, old=None):
        if old is None:
            self.left_bank = Bank[:]
            self.right_bank = []
            self.boat = LEFT
        else:
            self.left_bank = old.left_bank[:]
            self.right_bank = old.right_bank[:]
            self.boat = old.boat


    def __eq__(self, s2):
        if sorted(self.left_bank) != sorted(s2.left_bank): return False
        if sorted(self.right_bank) != sorted(s2.right_bank): return False
        if self.boat != s2.boat: return False
        return True
    
    def __str__(self):
        return "\nLeft Bank: " + str(sorted(self.left_bank)) + "\nRight Bank: " + \
               str(sorted(self.right_bank)) + \
               "\nBoat is on the " + ("left" if self.boat == LEFT else "right") + " bank."
    
    def __hash__(self):
        return (self.__str__()).__hash__()
    
    def copy(self):
        return State(old=self)
    
    def can_move(self, x, y=None):
        news = self.copy()
        if news.boat == LEFT:
            if x not in news.left_bank:
                return False
            if y is not None and y not in news.left_bank:
                return False
        else:
            if x not in news.right_bank:
                return False
            if y is not None and y not in news.right_bank:
                return False

        next_state = news.move(x, y)
        if 'farmer' not in next_state.left_bank and 'farmer' not in next_state.right_bank:
            return False

        if 'fox' in next_state.left_bank and 'chicken' in next_state.left_bank and 'farmer' not in next_state.left_bank:
            return False
        if 'fox' in next_state.right_bank and 'chicken' in next_state.right_bank and 'farmer' not in next_state.right_bank:
            return False

        if 'chicken' in next_state.left_bank and 'grain' in next_state.left_bank and 'farmer' not in next_state.left_bank:
            return False
        if 'chicken' in next_state.right_bank and 'grain' in next_state.right_bank and 'farmer' not in next_state.right_bank:
            return False
        
        return True
    
    def move(self, x, y=None):
        news = self.copy()

        if news.boat == LEFT:
            news.left_bank.remove(x)
            news.right_bank.append(x)
            if y is not None:
                news.left_bank.remove(y)
                news.right_bank.append(y)
        else:
            news.right_bank.remove(x)
            news.left_bank.append(x)
            if y is not None:
                news.right_bank.remove(y)
                news.left_bank.append(y)
        
        news.boat = RIGHT if news.boat == LEFT else LEFT
        return news
    
    def is_goal(self):
        return len(self.left_bank) == 0 and self.boat == RIGHT

class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)

# Put your INITIAL STATE section here.
CREATE_INITIAL_STATE = lambda : State()

# Put your OPERATORS section here.
OPERATORS = [Operator("Farmer crosses alone", lambda s: s.can_move('farmer'), lambda s: s.move('farmer')),
             Operator("Farmer crosses with fox", lambda s: s.can_move('farmer', 'fox'), lambda s: s.move('farmer', 'fox')),
             Operator("Farmer crosses with chicken", lambda s: s.can_move('farmer', 'chicken'), lambda s: s.move('farmer', 'chicken')),
             Operator("Farmer crosses with grain", lambda s: s.can_move('farmer', 'grain'), lambda s: s.move('farmer', 'grain'))]

# etc.


# Finish off with the GOAL_TEST and GOAL_MESSAGE_FUNCTION here.
def GOAL_TEST(s):
    return s.is_goal()

def GOAL_MESSAGE_FUNCTION(s):
    return "Congratulations on successfully transporting the farmer, fox, chicken, and grain!"