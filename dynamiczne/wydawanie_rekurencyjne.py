def wydaj(wartosc, nominaly):
    if wartosc == 0:
        return 0

    min_liczba_monet = wartosc+1
    for nominal in nominaly:
        if wartosc - nominal >= 0:
            liczba_monet = wydaj(wartosc - nominal, nominaly) + 1
            min_liczba_monet = min(min_liczba_monet, liczba_monet)
    return min_liczba_monet

print(wydaj(80, [25, 20, 1]))