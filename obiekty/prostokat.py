from obiekty.punkt import Punkt

class Prostokat:
    def __init__(self, lewy_gorny_punkt, szerokosc, wysokosc):
        self.lewy_gorny_punkt = lewy_gorny_punkt
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole(self):
        return self.wysokosc * self.szerokosc

if __name__ == '__main__':
    lg = Punkt(5, 10)
    print(lg.x, lg.y)

    pr = Prostokat(lg, 20,  30)
    print(pr.pole())