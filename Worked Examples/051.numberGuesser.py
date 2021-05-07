"""
Number Guesser Program

This is an example of how to use variables to 
keep track of information in a program that 
also makes use of loops
"""
import random 

def main():
    attempts = 0
    lower_limit = 1
    higher_limit = 100

    while True:
        num = random.randint(lower_limit, higher_limit)
        response = input(f'Is your number {num}? ')
        attempts += 1
        if response == 'lower':
            higher_limit = num
        elif response == 'higher':
            lower_limit = num
        elif response == 'correct':
            break
    
    print(f'I win! It took me {attempts} guesses')
    


if __name__ == "__main__":
    main()