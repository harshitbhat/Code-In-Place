def main():
    # TODO write your solution here
    height = int(input('Enter your height in meters: '))
    if height < 1.6:
        print("Below minimum astronaut height")
    elif height <= 1.9:
        print("Correct height to be an astronaut")
    else:
        print("Above maximum astronaut height") 

if __name__ == "__main__:
    main()