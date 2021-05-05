from karel.stanfordkarel import *

"""
File: SlotsKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""
def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def main():
    for i in range(3):
        turn_right()
        move()
        put_beeper()
        turn_around()
        move()
        turn_right()
        move()

if __name__ == "__main__":
    run_karel_program('Slots.w')