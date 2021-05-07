def main():
    m = int(input('Enter kilos of mass: '))
    C = 299792458
    e = m * C ** 2
    print('e = m * C^2...')
    print(f'm = {m * 1.0} kg')
    print(f'C = {C} m/s')
    print(f'{e} joules of energy!')

if __name__ == "__main__":
    main()