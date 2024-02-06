def bubble_sort_with_counts(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr, comparisons, swaps

def test_bubble_sort(array):
    sorted_array, comparisons, swaps = bubble_sort_with_counts(array.copy())
    print("Original Array:", array)
    print("Sorted Array:", sorted_array)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)
    print()

# Test arrays of increasing size
array1 = [5, 2, 9, 1, 5]
array2 = [8, 3, 6, 2, 7, 1, 4, 9]
array3 = [12, 6, 2, 9, 5, 7, 10, 1, 8, 3]
array4 = [15, 8, 4, 11, 2, 10, 7, 14, 1, 6, 12, 3, 9, 5, 13]

test_bubble_sort(array1)
test_bubble_sort(array2)
test_bubble_sort(array3)
test_bubble_sort(array4)
