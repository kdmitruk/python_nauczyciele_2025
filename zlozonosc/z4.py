def fun1(arr1, arr2):
    for i in range(0, len(arr1)):
        print(arr1[i])
    for j in range(0, len(arr2)):
        print(arr2[j])

# O(N, K) = N + K

def fun2(arr1, arr2):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            print(arr1[i] + arr2[j])

# O(N, K) = N * K

def fun3(arr1, arr2):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            for k in range (0, 10):
                print(arr1[i] + arr2[j] + k)

# T(N, K) = N * K * 10
# O(N, K) = N * K

def fun4(n):
    i = 1
    while i * i <= n:
        print(i, end=" ")
        i += 1

#O(N) = sqrt(N)

dane1 = [3, 7, 9, 12, 19, 30, 41, 56, 71]
dane2 = [8, 4, 2, 8, 1]

#fun1(dane1, dane2)

fun4(100)

