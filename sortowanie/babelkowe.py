dane = [1, 6, 5, 8, 2]

n = len(dane)

for i in range(n-1):
    for j in range(n-1-i):
        if dane[j] > dane[j+1]:
            dane[j], dane[j+1] = dane[j+1], dane[j]

print(dane)