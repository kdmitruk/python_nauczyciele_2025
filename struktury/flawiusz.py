class Osoba:
    def __init__(self, numer):
        self.numer = numer
        self.nastepny = None

# n - ilu ich jest
# k - co ilu zabijamy
def oblicz(n, k):
    pierwszy = Osoba(0)
    poprzedni = pierwszy

    for i in range(1, n):
        aktualny = Osoba(i)
        poprzedni.nastepny = aktualny
        poprzedni = aktualny

    aktualny.nastepny = pierwszy
    aktualny = pierwszy

    while aktualny != aktualny.nastepny:
        for i in range(k - 1):
            aktualny = aktualny.nastepny

        ofiara = aktualny.nastepny
        aktualny.nastepny = ofiara.nastepny

    return aktualny.numer

if __name__ == '__main__':
    print(oblicz(41, 3))
