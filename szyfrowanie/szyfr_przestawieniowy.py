import math

def indeksy_klucza(klucz):
    posortowany_klucz = sorted(klucz)
    return [posortowany_klucz.index(znak) for znak in klucz]
    # wynik = []
    # for znak in klucz:
    #     wynik.append(posortowany_klucz.index(znak))
    # return wynik

def szyfruj(napis, klucz):
    kolumny = len(klucz)
    wiersze = math.ceil(len(napis) / len(klucz))
    rozmiar = kolumny * wiersze
    wiadomosc = napis + '_' * (rozmiar - len(napis))
    kolejnosc = indeksy_klucza(klucz)

    zaszyfrowana_wiadomosc = ""
    for wiersz in range(wiersze):
        poczatek = wiersz * len(klucz)
        koniec = (wiersz+1) * len(klucz)
        linia = wiadomosc[poczatek:koniec]
        zaszyfrowana_linia = ''.join([linia[i] for i in kolejnosc])
        zaszyfrowana_wiadomosc += zaszyfrowana_linia
    return zaszyfrowana_wiadomosc

def odszyfruj(napis, klucz):
    pass

if __name__ == '__main__':
    napis = "Ala_ma_kota"
    klucz = "pies"

    zaszyfrowany_napis = szyfruj(napis, klucz)
    print(zaszyfrowany_napis)

    odszyfrowany_napis = odszyfruj(zaszyfrowany_napis, klucz)
    #print(odszyfrowany_napis)