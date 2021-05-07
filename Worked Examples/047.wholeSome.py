def main():
    affirmation = 'I am capable of doing anything I put my mind to.'
    ans = input('Please type the following affirmation: I am capable of doing anything I put my mind to.')
    while ans != affirmation:
        print('That was not the affirmation.')
        ans = input('Please type the following affirmation: I am capable of doing anything I put my mind to.')
    print('That\'s right! :)')
if __name__ == "__main__":
    main()