import matplotlib.pyplot as plt

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[],
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, left, right, ax, slupki):
    if left < right:
        for slupek in slupki:
            slupek.set_color('blue')
        for i in range(left, right + 1):
            slupki[i].set_color('red')

        mid = (left + right) // 2

        mergeSort(arr, left, mid, ax, slupki)
        mergeSort(arr, mid + 1, right, ax, slupki)
        merge(arr, left, mid, right)

    for slupek, wartosc in zip(slupki, arr):
        slupek.set_height(wartosc)
    plt.pause(0.4)


# Driver code
if __name__ == "__main__":
    arr = [5,78,2,56,17, 90, 5,26, 3, 32]

    plt.ion()
    fig, ax = plt.subplots()
    slupki = ax.bar(range(len(arr)), arr)

    mergeSort(arr, 0, len(arr) - 1, ax, slupki)
    for i in arr:
        print(i, end=" ")
    print()

    plt.ioff()
    plt.show()

# O(N) = N logN
# M(N) = N