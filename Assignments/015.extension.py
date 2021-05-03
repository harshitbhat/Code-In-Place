"""
TODO: Write a description here
"""

import random 

def main():
    n = int(input('Enter a number: '))
    steps = 0
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            print(f'{n} is even, so I take half: {n // 2}')
            n = n // 2
        else:
            print(f'{n} is odd, so I make 3n + 1: {3*n + 1}')
            n = 3 * n + 1
        steps += 1

    print(f'The process took {steps} steps to reach 1')
if __name__ == "__main__":
    main()