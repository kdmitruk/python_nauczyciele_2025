def brute_force(dane, szukana):
    for i in range(len(dane)):
        if dane[i] == szukana:
            print("znalazłem")
            return i
        else:
            print("nie znalazłem")
    return None

if __name__ == '__main__':
    dane = [3, 7, 9, 12, 19, 30, 41, 56]
    print(brute_force(dane, 112))