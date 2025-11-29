from obiekty.ulamek import Ulamek

class UlamekZlozony(Ulamek):
    def __init__(self,  licznik, mianownik):
        super().__init__(mianownik + licznik, mianownik)

    def __str__(self):
        return f"{self.licznik // self.mianownik} {self.licznik % self.mianownik}/{self.mianownik}"


if __name__ == '__main__':
    u1 = UlamekZlozony(3,2)
    u2 = UlamekZlozony(1,4)
    print(u1)
    print(u1+u2)
