from karel.stanfordkarel import *

"""
File: TensKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""
def put_ten_beepers():
    for i in range(10):
        put_beeper()

def main():
    while front_is_clear():
        put_ten_beepers()
        move()
    put_ten_beepers()

if __name__ == "__main__":
    run_karel_program('TensKarel1.w')