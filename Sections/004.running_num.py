"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""
import sys

def main():
    running_total = 0
    max_num = -sys.maxsize - 1
    min_num = sys.maxsize
    while True:
        num = int(input('Enter a value: '))
        if num == 0:
            break
        running_total += num
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        print(f'Running total is ${running_total}')
        print(f'Maximum so far is ${max_num}')
        print(f'Minimum so far is ${min_num}')
        print()

if __name__ == '__main__':
    main()