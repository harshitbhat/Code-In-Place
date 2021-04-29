"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""
import random

def main():
    # Fill this function out!
    responses = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not to tell you now.',
        'Cannot predict now. ',
        'Concentrate and ask again.',
        'Don\'t count on it. '
    ]
    question = input('Ask a yes or no question: ')
    ans = responses[random.randint(0, 5)]
    print(ans)

if __name__ == "__main__":
    main()