def wyszukaj_przez_haszowanie(sprawdzany, szukany):
    suma = 0
    suma_szukanego = 0

    for i in range(len(szukany)):
        suma_szukanego += ord(szukany[i])

    for i in range(len(szukany)-1):
        suma += ord(sprawdzany[i])

    for i in range(len(sprawdzany) - len(szukany) + 1):
        suma += ord(sprawdzany[i+len(szukany)-1])
        if suma == suma_szukanego:
            znaleziono = True
            for j in range(len(szukany)):
                if not sprawdzany[i+j] == szukany[j]:
                    znaleziono = False
                    break
            if znaleziono:
                return i
        suma -= ord(sprawdzany[i])

if __name__ == '__main__':
    sprawdzany = "Ala ma koguta i kota"
    szukany = "ko"
    print(wyszukaj_przez_haszowanie(sprawdzany, szukany))