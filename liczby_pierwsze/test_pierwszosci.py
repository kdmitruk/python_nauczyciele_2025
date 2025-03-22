def czy_pierwsza(liczba : int):
    if liczba < 2:
        return False

    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(czy_pierwsza(5))