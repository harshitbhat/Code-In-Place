from karel.stanfordkarel import *

"""
File: Archway.py
------------------------------
Karel will move up and over the archway.
"""
def turn_right():
    for i in range(3):
        turn_left()

def main():
    turn_left()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()