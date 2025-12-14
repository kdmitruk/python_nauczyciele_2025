def pierwszenstwo(operator):
    if  operator in ['-', '(']:
        return 0
    elif operator in ['+']:
        return 1
    elif operator in ['*', '/']:
        return 2
    return None

def infiksowa_do_postfiksowej(wejscie):
    wyjscie = []
    stos = []

    for token in wejscie:
        if token in ['+', '-', '*', '/']:
            while stos and pierwszenstwo(stos[-1]) >= pierwszenstwo(token):
                wyjscie.append(stos.pop())
            stos.append(token)
        elif token == '(':
            stos.append(token)
        elif token == ')':
            while stos and stos[-1] != '(':
                wyjscie.append(stos.pop())
            stos.pop() # na pewno '('
        else:
            wyjscie.append(token)

    while stos:
        wyjscie.append(stos.pop())

    return wyjscie

def oblicz(wejscie):
    stos = []
    for token in wejscie:
        if token in ['+', '-', '*', '/']:
            operand_prawy = stos.pop()
            operand_lewy = stos.pop()

            wynik = None
            match(token):
                case '+':
                    wynik = operand_lewy + operand_prawy
                case '-':
                    wynik = operand_lewy - operand_prawy
                case '*':
                    wynik = operand_lewy * operand_prawy
                case '/':
                    wynik = operand_lewy / operand_prawy

            stos.append(wynik)
        else:
            stos.append(float(token))
    return stos.pop()

if __name__ == '__main__':
    wyrazenie = "12 + 2 * ( 3 * 4 + 10 / 5 )"
    wyrazenie = wyrazenie.split(" ")
    wyrazenie_postfiksowe = infiksowa_do_postfiksowej(wyrazenie)
    print(" ".join(wyrazenie_postfiksowe))
    wynik = oblicz(wyrazenie_postfiksowe)
    print(wynik)