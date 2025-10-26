def znajdz_indeksy(dane, suma):
    for i in range(len(dane)): # N
        for j in range(len(dane)): # N^2
            if i != j: # N^2
                if dane[i] + dane[j] == suma: # N*(N-1)
                    return i, j
    return None

# O(N) = N^2

def znajdz_indeksy_v2(dane, suma):
    for i in range(len(dane)-1):  # N-1
        for j in range(i+1, len(dane)): # (N-1)N/2 = (N^2-N)/2 ---> N^2
            if dane[i] + dane[j] == suma:
                return i, j

# T(N) = N(N-1)/2
# O(N) = N^2

dane = [3, 7, 9, 12, 19, 30, 41, 56, 71]
szukana_suma = 60

print(znajdz_indeksy_v2(dane, szukana_suma))