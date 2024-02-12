import time
import matplotlib.pyplot as plt
import numpy as np

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

# Measure execution time for different input sizes
input_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
execution_times = []

for size in input_sizes:
    arr = list(range(size, 0, -1))  # Input in descending order
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    execution_times.append(end_time - start_time)

# Plot the results
plt.plot(input_sizes, execution_times, marker='o', linestyle='-')
plt.xscale('log')  # Use log scale for better visualization
plt.yscale('log')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Quicksort Worst-Case Complexity')
plt.show()
