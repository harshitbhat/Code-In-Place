from karel.stanfordkarel import *

"""
File: BloomFlower.py
------------------------------
Karel will scale the stem of the flower she's facing, bloom the flower with 4 beepers, and return to the ground.
Karel should end up in the bottommost row, directly to the right of the stem, facing East.
"""
def turn_right():
    for i in range(3):
        turn_left()

def climb_stem():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
    turn_left()

def bloom():
    for i in range(3):
        put_beeper()
        move()
        turn_right()
    put_beeper()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()
    turn_left()

def main():
    climb_stem()
    bloom()
    move_to_wall()

if __name__ == "__main__":
    run_karel_program()