"""
Prints the Fizz Buzz sequence up to a given number.
"""

def main():
    fizzed = 0
    buzzed = 0
    fizzbuzzed = 0

    num = int(input('Nuber to count to: '))
    for i in range(1,num+1):
        if i % 15 == 0:
            print('Fizzbuzz')
            fizzbuzzed += 1
        elif i % 5 == 0:
            print('Buzz')
            buzzed += 1
        elif i % 3 == 0:
            print('Fizz')
            fizzed += 1
        else:
            print(i)

    print()
    print(f'Num fizzed: {fizzed}')
    print(f'Num buzzed: {buzzed}')
    print(f'Num fizzbuzzed: {fizzbuzzed}')
 
if __name__ == '__main__':
    main()