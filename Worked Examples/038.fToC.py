def main():
    f = float(input('Enter temperature in Fahrenheit: '))
    c = ((f - 32) * 5 ) / 9
    print(f'Temperature: {f}F = {c}C')
if __name__ == "__main__":
    main()