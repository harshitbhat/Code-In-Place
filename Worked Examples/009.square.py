from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Make Karel place beepers in a square (4 beepers total)
and end in the same position Karel starts in.
"""

def main():
    for i in range(4):
        put_beeper()
        move()
        turn_left()

if __name__ == "__main__":
    run_karel_program()