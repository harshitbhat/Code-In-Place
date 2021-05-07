from karel.stanfordkarel import *

"""
File: TreasureHunt2.py
------------------------------
Karel will move forward until a beeper.
At every beeper, Karel will turn left and move until the next beeper, until Karel is standing on the treasure, which is a pile of 10 beepers.
"""

def turn_right():
    for i in range(3):
        turn_left()

def main():
    while no_beepers_present():
        move()
        if beepers_present():
            while beepers_present():
                pick_beeper()
            turn_left()
            if front_is_blocked():
                turn_right()
                turn_right()

if __name__ == "__main__":
    run_karel_program()