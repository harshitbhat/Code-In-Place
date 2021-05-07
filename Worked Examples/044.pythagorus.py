import math

def main():
    a = int(input('Enter the length of AB: '))
    b = int(input('Enter the length of AC: '))
    print(f'The length of BC (the hypotenuse) is: {math.sqrt(a**2 + b**2)}')
if __name__ == "__main__":
    main()