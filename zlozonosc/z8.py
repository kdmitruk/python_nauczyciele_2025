def f_rekurencyjny(n):
    if n<2:
        return n
    else:
        return f_rekurencyjny(n - 1) + f_rekurencyjny(n - 2)

# O(N) = N logN
# M(N) = N

def f_iteracyjny(n):
    if n<2:
        return n
    fn_1 = 1
    fn_2 = 0
    for _ in range(2, n+1):
        fn = fn_2 + fn_1
        fn_2 = fn_1
        fn_1 = fn
    return fn

# O(N) = N
# M(N) = 1

def f_iteracyjny_skrocony(n):
    if n<2:
        return n
    fn_2, fn_1 = 0, 1
    for _ in range(2, n+1):
       fn_2, fn_1 = fn_1, fn_2 + fn_1
    return fn_1

# O(N) = N
# M(N) = 1

def f_rekurencja_ogonowa(n, fn_2 = 0 , fn_1 = 1):
    if n == 0:
        return fn_2
    elif n == 1:
        return fn_1
    else:
        return f_rekurencja_ogonowa(n-1, fn_1, fn_2 + fn_1)

# O(N) = N
# M(N) = N


if __name__ == '__main__':
    print(f_rekurencja_ogonowa(50))

