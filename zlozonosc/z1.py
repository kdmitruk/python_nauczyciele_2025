def pomnoz_przez_2(dane):
    for i in range(len(dane)):
        dane[i] *= 2

dane = [3, 7, 9, 12, 19, 30, 41, 56, 71]
pomnoz_przez_2(dane)
print(dane)

# T(n) = n
# O(n) = n

