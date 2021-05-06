from karel.stanfordkarel import *

"""
File: UpstairsDownstairs.py
------------------------------
Karel will climb three stair steps up and then three stair steps down.
"""
def turn_right():
    for i in range(3):
        turn_left()

def move_up():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
        move()

def move_down():
    while front_is_clear():
        move()
        turn_right()
        move()
        turn_left()

def main():
    move_up()
    move_down()
if __name__ == "__main__":
    run_karel_program('UpstairsDownstairs.w')