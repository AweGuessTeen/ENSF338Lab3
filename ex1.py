import sys 
sys.setrecursionlimit(20000)

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):

    size1 = mid - low + 1
    size2 = high - mid

    L = [0] * size1
    R = [0] * size2

    for i in range(size1):
        L[i] = arr[low + i]

    for j in range(size2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = low

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


arr = [8, 42, 25, 3, 3, 2, 27, 3]
print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
