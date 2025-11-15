from math import gcd

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        self.__zredukuj()

    def czy_calkowita(self):
        return self.licznik % self.mianownik == 0

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def __float__(self):
        return self.licznik / self.mianownik

    def __zredukuj(self):
        nwd = gcd(self.licznik, self.mianownik)
        self.licznik //= nwd
        self.mianownik //= nwd

    def pomnoz(self, inny):
        return Ulamek(
            self.licznik * inny.licznik,
            self.mianownik * inny.mianownik
        )

def porownaj(a: Ulamek, b: Ulamek):
    wartosc_a = float(a)
    wartosc_b = float(b)
    if wartosc_a < wartosc_b: return -1
    elif wartosc_a == wartosc_b: return 0
    else: return 1

if __name__ == '__main__':
    u1 = Ulamek(2, 3)
    u2 = Ulamek(3, 4)
    print(u1.pomnoz(u2))

    #print(float(u))
    #print(porownaj(Ulamek(2, 3), Ulamek(3,  4)))