dane = [1, 6, 5, 8, 2]

for i in range(1, len(dane)):
    aktualny = dane[i]
    for j in range(i):
        if aktualny < dane[j]:
            dane.pop(i)
            dane.insert(j, aktualny)
            break

print(dane)