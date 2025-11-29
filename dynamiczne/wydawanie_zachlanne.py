def wydaj(wartosc, nominaly):
    licznik = 0
    nominaly = sorted(nominaly)
    nominaly.reverse()

    for nominal in nominaly:
        print(nominal, wartosc // nominal)

        licznik += wartosc // nominal
        wartosc = wartosc % nominal

    if wartosc == 0:
        return licznik
    else:
        return "nie da się wydać"

print(wydaj(23, [1, 2, 5]))