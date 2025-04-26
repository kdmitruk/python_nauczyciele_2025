alfabet = list("aąbcćdeęfghijklłmnopqrsśtuvwxyzźż")

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
    napis = "eax toćę ksbax khlwex, fhsmws?"
    for klucz in range(len(alfabet)):
        odszyfrowany_napis = odszyfruj(napis, klucz)
        print(odszyfrowany_napis)
