def koszt_przejscia(dane):
    liczba_wierszy = len(dane)
    liczba_kolumn = len(dane[0])

    wynik = dane[0][0]
    x = 0
    y = 0

    while x < liczba_kolumn and y < liczba_wierszy:
        if x == liczba_kolumn - 1 and y == liczba_wierszy - 1:
            return wynik
        elif y == liczba_kolumn:
            x += 1
        elif x == liczba_wierszy:
            y += 1
        else:
            prawo = dane[y][x+1]
            dol = dane[y+1][x]

            if prawo < dol:
                x += 1
            else:
                y += 1
        print(dane[y][x])
        wynik += dane[y][x]
    return None


dane = [
    [3,  2, 12, 15, 10],
    [6, 19,  7, 11, 17],
    [8,  5, 12, 32, 21],
    [3, 20,  2,  9,  7]
]

print(koszt_przejscia(dane))