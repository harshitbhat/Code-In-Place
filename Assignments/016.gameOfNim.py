"""
TODO: Write a description here
"""

import random

def main():
    stones = 20
    player = 1

    while stones > 0:
        print(f'There are {stones} stones left')
        toRemove = int(input(f'Player {player} would you like to remove 1 or 2 stones? '))
        if toRemove != 1 and toRemove != 2:
            validInput = False
            while not validInput:
                toRemove = int(input('Please enter 1 or 2: '))
                if toRemove == 1 or toRemove == 2:
                    validInput = True
        stones -= toRemove
        if player == 1:
            player = 2
        else:
            player = 1
        print()

    print(f'Player {player} wins!')

if __name__ == '__main__':
    main()