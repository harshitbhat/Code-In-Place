from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Here is a place to program your Section problem
def turn_right():
    for i in range(3):
        turn_left()

def make_hospital():
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_right()
    move()
    turn_right()
    for i in range(2):
        put_beeper()
        move()
    put_beeper()
    turn_left()
    move()
def main():
    while front_is_clear():
        move()
        if beepers_present():
            make_hospital()

if __name__ == '__main__':
    run_karel_program('HospitalKarel.w')