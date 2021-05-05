from karel.stanfordkarel import *

"""
File: InvertKarel.py
-----------------------
Inverts the pattern of beepers in a single row world.
"""
def invert():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

def main():
    while front_is_clear():
        invert()
        move()
    invert()

if __name__ == "__main__":
    run_karel_program('Invert1.w')