def potega(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    elif wykladnik % 2 == 0:
        p = potega(podstawa, wykladnik // 2)
        return p * p
    else:
        return podstawa * potega(podstawa, wykladnik - 1)

if __name__ == '__main__':
    print(potega(5, 6))