class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

if __name__ == '__main__':
    u = Ulamek(3, 4)
    print(u.licznik, u.mianownik)