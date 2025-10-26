import matplotlib.pyplot as plt

def sortuj_babelkowo(dane):
    n = len(dane)

    plt.ion()
    fig, ax = plt.subplots()
    slupki = ax.bar(range(len(dane)), dane)

    for i in range(n-1):
        for j in range(n-1-i):

            for slupek in slupki:
                slupek.set_color('blue')
            slupki[j].set_color('orange')
            slupki[j+1].set_color('orange')
            plt.pause(0.2)

            if dane[j] > dane[j+1]:
                dane[j], dane[j+1] = dane[j+1], dane[j]

                for slupek, wartosc in zip (slupki, dane):
                    slupek.set_height(wartosc)

                plt.pause(0.4)

    plt.ioff()
    plt.show()

if __name__ == '__main__':
    dane = [5,78,2,56,17, 90, 5,26, 3, 32]
    sortuj_babelkowo(dane)
    print(dane)

#O(N) = N^2