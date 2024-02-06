# Imports
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Definitions
def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, key, 0, i - 1)

        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]

        arr[pos] = key

def binary_search(arr, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return low

# Main Code
input_lengths = [10, 50, 100, 200, 500, 1000]
trad_times = []
bin_times = []

for length in input_lengths:
    rand_array = generate_random_array(length)

    # Traditional insertion sort
    trad_time = timeit.timeit(stmt=lambda: insertion_sort(rand_array.copy()), number=1)
    trad_times.append(trad_time)
    print(f"Traditional Insertion Sort for length {length}: {trad_time:.6f} seconds")

    # Binary insertion sort
    bin_time = timeit.timeit(stmt=lambda: binary_insertion_sort(rand_array.copy()), number=1)
    bin_times.append(bin_time)
    print(f"Binary Insertion Sort for length {length}: {bin_time:.6f} seconds")

    print("")

# Plotting
plt.plot(input_lengths, trad_times, label='Insertion Sort', marker='o')
plt.plot(input_lengths, bin_times, label='Binary Insertion Sort', marker='o')

plt.title('Insertion Sort vs Binary Insertion Sort')
plt.xlabel('Array Length')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.show()

'''
4. Discuss the results: which algorithm is faster? Why?
        By analyzing the plot displayed at the end of this program. It's clear that
        the binary insertion sort is faster than a traditional insertion sort.
        This becomes more evident as the input length becomes larger and larger, as
        the gap between each sorting algorithm becomes wider and wider.
'''