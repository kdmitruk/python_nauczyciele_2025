def plecak(wartosci, wagi, max_waga, i=0):
    if i == len(wartosci):
        return 0
    elif wagi[i] > max_waga:
        return plecak(wartosci, wagi, max_waga, i+1)
    else:
        wartosc_plecaka_jezeli_wloze = wartosci[i] + plecak(wartosci, wagi, max_waga - wagi[i], i+1)
        wartosc_plecaka_jezeli_nie_wloze = plecak(wartosci, wagi, max_waga, i+1)
        return max(wartosc_plecaka_jezeli_wloze, wartosc_plecaka_jezeli_nie_wloze)

wartosci = [20, 30, 15, 25, 10]
wagi = [6, 13, 5, 10, 3]
max_waga = 20

print(plecak(wartosci, wagi, max_waga))

