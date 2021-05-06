from karel.stanfordkarel import *

"""
File: FiveCorridorsKarel.py
-----------------------
Karel traverse 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
"""
def move_to_end():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def put_in_tunnel():
    turn_right()
    move_to_end()
    if beepers_present():
        pick_beeper()
    put_beeper()
    turn_around()
    move_to_end()
    turn_right()

def main():
    turn_left()
    while front_is_clear():
        put_in_tunnel()
        move()
    put_in_tunnel()
    turn_right()

if __name__ == "__main__":
    run_karel_program()