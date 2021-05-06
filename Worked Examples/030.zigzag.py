from karel.stanfordkarel import *

"""
File: ZigZagKarel.py
-----------------------
Places a zig zag pattern of beepers in the world.
"""
def turn_right():
    for i in range(3):
        turn_left()

def make_pattern():
    put_beeper()
    move()
    turn_left()
    move()
    put_beeper()
    turn_right()
    turn_right()
    move()
    turn_left()

def main():
    while front_is_clear():
        make_pattern()
        if front_is_clear():
            move()

    

if __name__ == "__main__":
    run_karel_program('ZigZag2.w')