import random

alfabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + list("ąćęłóźż")
random.shuffle(alfabet)

def szyfruj(napis, klucz):
    szyfr = [alfabet[(i + klucz) % len(alfabet)] for i in range(len(alfabet))]
    wynik = ""
    for znak in napis:
        if znak in alfabet:
            zaszyfrowany_znak = szyfr[alfabet.index(znak)]
            wynik += zaszyfrowany_znak
        else:
            wynik += znak
    return wynik

def odszyfruj(napis, klucz):
    szyfr = [alfabet[(i + klucz) % len(alfabet)] for i in range(len(alfabet))]
    wynik = ""
    for znak in napis:
        if znak in alfabet:
            zaszyfrowany_znak = alfabet[szyfr.index(znak)]
            wynik += zaszyfrowany_znak
        else:
            wynik += znak
    return wynik

if __name__ == '__main__':
    napis = "Ala ma żółć"
    klucz = 3

    zaszyfrowany_napis = szyfruj(napis, klucz)
    print(zaszyfrowany_napis)

    odszyfrowany_napis = odszyfruj(zaszyfrowany_napis, klucz)
    print(odszyfrowany_napis)
