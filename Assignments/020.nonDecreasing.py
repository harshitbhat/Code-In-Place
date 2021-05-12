def main():
    # TODO write your solution here
    print('Enter a sequence of non-decreasing numbers.')
    prev = int(input('Enter num: '))
    sequence = 1
    while True:
        cur = int(input('Enter num: '))
        if cur >= prev:
            prev = cur
            sequence += 1
        else:
            print('Thanks for playing!')
            print(f'Sequence length: {sequence}')
            break


if __name__ == "__main__":
    main()