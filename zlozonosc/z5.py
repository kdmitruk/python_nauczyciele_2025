def sortuj_babelkowo(dane):
    n = len(dane)

    for i in range(n-1):
        for j in range(n-1-i):
            if dane[j] > dane[j+1]:
                dane[j], dane[j+1] = dane[j+1], dane[j]

if __name__ == '__main__':
    dane = [5,78,2,56,5,26]
    sortuj_babelkowo(dane)
    print(dane)

#O(N) = N^2