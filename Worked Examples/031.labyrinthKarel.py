from karel.stanfordkarel import *

"""
File: LabyrinthKarel.py
------------------------------
Karel solves labyrinths!
"""
def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def find_direction():
    turn_left()
    if front_is_blocked():
        turn_around()

def main():
    while front_is_clear():
        move_to_wall()
        find_direction()
        
if __name__ == "__main__":
    run_karel_program('Labyrinth2')