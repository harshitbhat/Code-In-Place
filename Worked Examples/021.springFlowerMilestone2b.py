from karel.stanfordkarel import *

"""
File: ClimbStem.py
------------------------------
Karel will climb a "stem" -- Karel should start facing a wall. Karel will turn and scale the wall until there is no more wall to Karel's right.
"""
def turn_right():
    for i in range(3):
        turn_left()

def main():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
if __name__ == "__main__":
    run_karel_program()