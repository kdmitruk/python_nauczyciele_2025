dane = [1, 6, 5, 8, 2]
n = len(dane)

for i in range(n):
    pozycja = i
    minimum = dane[i]
    for j in range(i+1, n):
        if dane[j] < minimum:
            minimum = dane[j]
            pozycja = j
    if not pozycja == i:
        dane[pozycja], dane[i] = dane[i], dane[pozycja]

print(dane)