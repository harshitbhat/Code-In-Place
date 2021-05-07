from karel.stanfordkarel import *

"""
File: TreasureHunt1.py
------------------------------
Karel will move forward until a beeper.
At every beeper, Karel will turn left and move until the next beeper, until Karel is standing on the treasure, which is a pile of 10 beepers.
"""

def main():
    while no_beepers_present():
        move()
        if beepers_present():
            while beepers_present():
                pick_beeper()
            turn_left()

if __name__ == "__main__":
    run_karel_program('TreasureHunt1.w')