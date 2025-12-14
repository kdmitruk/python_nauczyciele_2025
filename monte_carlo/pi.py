# n - liczba testów
import random
import matplotlib.pyplot as plt


def oszacuj_pi(n):
    wewnatrz = 0
    for i in range(n):
        x = random.random()
        y = random.random()

        if x ** 2 + y ** 2 <= 1:
            wewnatrz += 1

    pi = 4 * wewnatrz / n
    return pi

def zilustruj_pi(n):
    wewnatrz = 0
    x_wewnatrz, y_wewnatrz, x_zewnatrz, y_zewnatrz = [], [], [], []

    for i in range(n):
        x = random.random()
        y = random.random()

        if x ** 2 + y ** 2 <= 1:
            wewnatrz += 1
            x_wewnatrz.append(x)
            y_wewnatrz.append(y)
        else:
            x_zewnatrz.append(x)
            y_zewnatrz.append(y)

    pi = 4 * wewnatrz / n

    plt.figure(figsize=(6, 6))
    plt.scatter(x_wewnatrz, y_wewnatrz, color='green', s=1)
    plt.scatter(x_zewnatrz, y_zewnatrz, color='red', s=1)

    plt.show()
    return pi



if __name__ == '__main__':
    print(zilustruj_pi(10000))
