def wydaj(wartosc, nominaly, pamiec):
    if wartosc in pamiec:
        return pamiec[wartosc]

    if wartosc == 0:
        return 0

    min_liczba_monet = wartosc+1
    for nominal in nominaly:
        if wartosc - nominal >= 0:
            liczba_monet = wydaj(wartosc - nominal, nominaly, pamiec) + 1
            min_liczba_monet = min(min_liczba_monet, liczba_monet)
    pamiec[wartosc] = min_liczba_monet
    return min_liczba_monet

print(wydaj(123, [25, 20, 1], {}))
