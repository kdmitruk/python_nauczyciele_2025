def wyswietl(liczba):

    if liczba > 0:
        wyswietl(liczba - 1)
    print(liczba)


if __name__ == '__main__':
    wyswietl(10)