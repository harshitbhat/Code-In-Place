"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Fill this function out!
    weightOnEarth = input('Enter a weight on Earth: ')
    weightOnMars = int(weightOnEarth) * 0.378
    print('The equivalent on Mars: ',weightOnMars)
    pass

if __name__ == "__main__":
    main()