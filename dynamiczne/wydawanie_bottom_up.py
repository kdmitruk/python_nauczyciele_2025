def wydaj(wartosc, nominaly):
    pamiec = [wartosc] * (wartosc + 1)
    pamiec[0] = 0
    for aktualna_wartosc in range(1, wartosc + 1):
        for nominal in nominaly:
            if aktualna_wartosc - nominal >= 0:
                pamiec[aktualna_wartosc] = min(pamiec[aktualna_wartosc], pamiec[aktualna_wartosc - nominal] + 1)
    return pamiec[wartosc]

print(wydaj(80, [25, 20, 1]))