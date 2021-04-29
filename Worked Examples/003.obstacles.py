from karel.stanfordkarel import *

"""
File: Obstacles.py
------------------------------
Karel will jump over the obstacles and put beepers in the pink squares.
"""
def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()


def put_in_obstacles():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    while front_is_clear():
       move()

def main():
   while front_is_clear():
       move()
   put_in_obstacles()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()