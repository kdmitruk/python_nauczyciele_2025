def koszt_przejscia(dane, y=0, x=0):
    liczba_wierszy = len(dane)
    liczba_kolumn = len(dane[0])

    if y == liczba_wierszy - 1 and x == liczba_kolumn - 1:
        return dane[y][x]
    elif y == liczba_wierszy - 1:
        return dane[y][x] + koszt_przejscia(dane, y, x + 1)
    elif x == liczba_kolumn - 1:
        return dane[y][x] + koszt_przejscia(dane, y + 1, x)
    else:
        prawo = koszt_przejscia(dane, y, x + 1)
        dol = koszt_przejscia(dane, y + 1, x)
        return dane[y][x] + min(prawo, dol)


dane = [
    [3,  2, 12, 15, 10],
    [6, 19,  7, 11, 17],
    [8,  5, 12, 32, 21],
    [3, 20,  2,  9,  7]
]

print(koszt_przejscia(dane))