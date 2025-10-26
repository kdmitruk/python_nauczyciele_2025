def silnia(n):
    if n>1:
        return n * silnia(n-1)
    else:
        return 1

if __name__ == '__main__':
    print(silnia(5))

# O(N) = N
# M(N) = N