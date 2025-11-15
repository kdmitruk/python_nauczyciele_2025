class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def czy_calkowita(self):
        return self.licznik % self.mianownik == 0

if __name__ == '__main__':
    u = Ulamek(8, 4)
    print(u.czy_calkowita())