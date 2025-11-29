def koszt_przejscia(dane):
    liczba_wierszy = len(dane)
    liczba_kolumn = len(dane[0])

    pamiec = [[0] * liczba_kolumn for _ in range(liczba_wierszy)]
    pamiec[0][0] = dane[0][0]
    for x in range(1, liczba_kolumn):
        pamiec[0][x] = dane[0][x] + pamiec[0][x-1]
    for y in range(1, liczba_wierszy):
        pamiec[y][0] = dane[y][0] + pamiec[y-1][0]
    for y in range(1, liczba_wierszy):
        for x in range(1, liczba_kolumn):
            gora = pamiec[y-1][x]
            lewo = pamiec[y][x-1]
            pamiec[y][x] = dane[y][x] + min(gora, lewo)
    return pamiec[liczba_wierszy - 1][liczba_kolumn - 1]

dane = [
    [3,  2, 12, 15, 10],
    [6, 19,  7, 11, 17],
    [8,  5, 12, 32, 21],
    [3, 20,  2,  9,  7]
]

print(koszt_przejscia(dane))