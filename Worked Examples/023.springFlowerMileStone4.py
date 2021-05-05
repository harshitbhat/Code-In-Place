from karel.stanfordkarel import *

"""
File: SpringFlowers.py
------------------------------
Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
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

def bloom_flower():
    climb_stem()
    bloom()
    move_to_wall()

def main():
    while front_is_clear():
        move()
        if front_is_blocked():
            bloom_flower()

if __name__ == "__main__":
    run_karel_program('SpringFlowers1.w')