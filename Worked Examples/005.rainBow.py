from karel.stanfordkarel import *

"""
File: Rainbow.py
------------------------------
Karel makes a rainbow!
"""


def main():
    paint_corner(RED)
    move()
    paint_corner(ORANGE)
    move()
    paint_corner(YELLOW)
    move()
    paint_corner(GREEN)
    move()
    paint_corner(BLUE)
    move()



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()