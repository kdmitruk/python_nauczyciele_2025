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


if __name__ == '__main__':
    wyrazenie = "12 + 2 * ( 3 * 4 + 10 / 5 )"
    wyrazenie = wyrazenie.split(" ")
    print(" ".join(infiksowa_do_postfiksowej(wyrazenie)))