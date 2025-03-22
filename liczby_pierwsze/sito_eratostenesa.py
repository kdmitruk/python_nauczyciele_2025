def generuj_liczby_pierwsze(n):
    dane = [True] * (n+1)
    dane[0] = dane[1] = False

    for i in range(2, n + 1):
        if dane[i] == True:
            for j in range(i * 2, n + 1, i):
                dane[j] = False

    for i in range(n+1):
        if dane[i] == True:
            print(i)

if __name__ == '__main__':
    generuj_liczby_pierwsze(120)