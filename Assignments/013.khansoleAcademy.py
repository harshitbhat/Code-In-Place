"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

def main():
    firstNumber = random.randint(10,99)
    secondNumber = random.randint(10,99)
    ans = firstNumber + secondNumber
    print(f'What is {firstNumber} + {secondNumber}?')
    userAnswer = int(input('Your answer: '))
    if ans ==  userAnswer:
        print('Correct!')
    else:
        print(f'Incorrect. The expected answer is {ans}')

if __name__ == '__main__':
    main()