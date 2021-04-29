from karel.stanfordkarel import *

"""
File: MoveBeeper.py
------------------------------
Karel will move the beeper up to the top of its column.
Karel starts in the bottom left corner, facing East, in front of the beeper, and Karel will end in the top right corner facing East.
"""
def turn_right():
    for i in range(3):
        turn_left()

def main():
   move()
   pick_beeper()
   turn_left()
   move()
   move()
   put_beeper()
   turn_right()
   move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()