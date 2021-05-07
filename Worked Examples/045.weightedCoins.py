import random

def main():
    roll = random.randint(1, 10)
    winner = 'heads'
    if roll > 7:
        winner = 'tails'
    print('winner)

if __name__ == "__main__":
    main()