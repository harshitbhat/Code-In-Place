"""
TODO: Write a description here
"""

import random

def main():
    totalCorrect = 3
    correct = 0

    while True:
        firstNumber = random.randint(10,99)
        secondNumber = random.randint(10,99)
        ans = firstNumber + secondNumber
        print(f'What is {firstNumber} + {secondNumber}?')
        userAnswer = int(input('Your answer: '))
        if ans ==  userAnswer:
            correct += 1
            print(f'Correct! You\'ve gotten {correct} correct in a row.')
            if(correct == totalCorrect):
                print('Congratulations! You mastered addition.')
                break
        else:
            correct = 0
            print(f'Incorrect. The expected answer is {ans}')

if __name__ == '__main__':
    main()