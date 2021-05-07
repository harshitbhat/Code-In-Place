def main():
    a = 0
    b = 1
    print(a)
    print(b)
    c = a + b
    while c < 10000:
        print(c)
        a = b
        b = c
        c = a + b

if __name__ == "__main__":
    main()