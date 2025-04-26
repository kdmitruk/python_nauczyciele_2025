def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def nwd_rekurencyjne(a, b):
    if a != b:
        if a > b:
            return nwd_rekurencyjne(a-b, b)
        else:
            return nwd_rekurencyjne(a, b-a)
    return a

def nwd_modulo(a, b):
    if a != 0:
        return nwd_modulo(b % a, a)
    return b

if __name__ == '__main__':
    print(nwd_modulo(348,192))