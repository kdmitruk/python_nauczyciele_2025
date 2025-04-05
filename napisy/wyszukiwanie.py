def wyszukaj_naiwnie(sprawdzany, szukany):
    for i in range(len(sprawdzany) - len(szukany) + 1):
        if sprawdzany[i:i+len(szukany)] == szukany:
            return i
    return None

if __name__ == '__main__':
    sprawdzany = "Ala ma tako"
    szukany = "ko"
    print(wyszukaj_naiwnie(sprawdzany, szukany))