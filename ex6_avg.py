# imports
import timeit
import random
import matplotlib.pyplot as plt

# Definitions
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Main Code
lengths = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
lin_results = []
bin_results = []

for length in lengths:
    target = random.randint(0, 100)
    numbers = random.sample(range(length), length)
    
    # Ensure that target exists in the array
    target_index = random.randint(0, length - 1)
    numbers[target_index] = target

    lin_times = []
    bin_times = []

    for _ in range(1000):
        random.shuffle(numbers)
        
        # Linear search
        lin_time = timeit.timeit(lambda: linear_search(numbers, target), number=100)
        lin_times.append(lin_time / 100)

        # Binary search
        bin_time = timeit.timeit(lambda: binary_search(quicksort(numbers), target), number=100)
        bin_times.append(bin_time / 100)

    avg_linear = sum(lin_times) / len(lin_times)
    avg_binary = sum(bin_times) / len(bin_times)

    print(f"Average time for list of length {length} with target {target}:")
    print(f"Linear Search: {avg_linear} seconds")
    print(f"Binary Search: {avg_binary} seconds")

    lin_results.append(avg_linear)
    bin_results.append(avg_binary)

# Plot
plt.plot(lengths, lin_results, label='Linear Search')
plt.plot(lengths, bin_results, label='Binary Search')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('List Length')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Linear Search vs. Binary Search')
plt.show()

'''
Question 4:
When comparing both algorithms, one might expect the second to be faster as the first is a simple linear search with an average-case complexity of O(n).
However, we must take into account that the second algorithm must first use quicksort to sort the arrays first before performing a binary searcch.
Therefore, especially when the input size becomes larger, the second algorithm takes more time to find its target. This can be seen both in the
average times and on the plot generated at the end of the entire test.
On the other hand, if we were to simply compare a binary search on a pre-sorted array, then this would be faster on average than a linear search.
'''