from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper on the middle of the first row.
"""
def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()
def move_to_end():
    while front_is_clear():
        move()
def move_beeper():
    if beepers_present():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        move()

def main():
    put_beeper()
    if front_is_clear():
        move_to_end()
        put_beeper()
        turn_around()
        move()

        while no_beepers_present():
            while no_beepers_present():
              move()
            move_beeper()
        pick_beeper()
        turn_around()
        move()

if __name__ == '__main__':
    run_karel_program('Midpoint.w')