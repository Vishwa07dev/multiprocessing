import random
import time


def merge(arr,l,m,r):
    size1 = m-l+1
    size2 = r-m
    L = arr[l:m+1]
    R = arr[m:r]
    i = 0
    j = 0
    k = l
    while i < size1 and j < size2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < size1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < size2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

if __name__ == '__main__':
    n = 100000
    arr = [random.randint(0, i * 100) for i in range(n)]
    print("Given array:")
    for i in range(n):
        print("%d" % arr[i],end=" "),
    start = time.perf_counter()
    mergeSort(arr, 0, n - 1)
    finish = time.perf_counter()
    print("\n\nSorted array:")
    for i in range(n):
        print("%d" % arr[i] ,end=" "),
    print()
    print(f'Finished in {round(finish - start, 2)}')