from karel.stanfordkarel import *

def main():
    # TODO write your solution here
    for i in range(4):
        if front_is_clear():
            move()
            move()
            make_wave()

def make_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_around()
    turn_right()

# There is no need to edit code beyond this point

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()