from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def make_pillar():
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        put_beeper()
        move()
    if beepers_present():
        pick_beeper()
    put_beeper()

def main():
    while front_is_clear():
        turn_left()
        while front_is_clear() :
            if beepers_present():
                # Write code to move to front and place beepers_present
                make_pillar()
            else:
                move()
        turn_around()
        while front_is_clear():
            move()
        turn_left()
        move()

    # For Last column
    turn_left()
    while front_is_clear() :
        if beepers_present():
            # Write code to move to front and place beepers_present
            make_pillar()
        else:
            move()
    turn_around()
    while front_is_clear():
        move()
    turn_left()

if __name__ == '__main__':
    run_karel_program('SampleQuad3.w')