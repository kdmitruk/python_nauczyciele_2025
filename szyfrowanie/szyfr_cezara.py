import random

alfabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + list("ąćęłóźż")
random.shuffle(alfabet)
print(alfabet)

def szyfruj(napis, klucz):
    szyfr = [alfabet[(i + klucz) % len(alfabet)] for i in range(len(alfabet))]
    print(szyfr)
    wynik = ""
    for znak in napis:
        if znak in alfabet:
            indeks = alfabet.index(znak)
            zaszyfrowany_znak = szyfr[indeks]
            wynik += zaszyfrowany_znak
        else:
            wynik += znak
    return wynik

def odszyfruj(napis, klucz):
    pass

if __name__ == '__main__':
    napis = "Ala ma żółć"
    klucz = 3

    zaszyfrowany_napis = szyfruj(napis, klucz)
    print(zaszyfrowany_napis)

    odszyfrowany_napis = odszyfruj(zaszyfrowany_napis, klucz)
    #print(odszyfrowany_napis)
