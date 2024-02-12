# Imports
import timeit
import random
import matplotlib.pyplot as plt

# Definitions
def binary(arr, target, start, end, initial):
    while start <= end:
        mid = (start + end) // 2 if initial is None else initial
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def find_mid(arr, target):
    midpoints = list(range(0, len(arr), len(arr)//10))  # You can adjust the number of midpoints as needed
    timings = []

    for midpoint in midpoints:
        search_time = timeit.timeit(lambda: binary(arr, target, 0, len(arr)-1, midpoint), number=10000)
            # Adjust the number of iterations as needed
        timings.append((midpoint, search_time))

    best_midpoint, _ = min(timings, key=lambda x: x[1])
    return best_midpoint, timings

# Main Code
arr = sorted([random.randint(0, 1000) for _ in range(1000)])
target = random.choice(arr)
best_mid, all_time = find_mid(arr, target)
print(f'Best Midpoint for Target {target}: {best_mid}')

midpoints = [midpoint for midpoint, _ in all_time]
timings = [time for _, time in all_time]

plt.scatter(midpoints, timings)
plt.title('Binary Search Performance with Different Midpoints')
plt.xlabel('Midpoint')
plt.ylabel('Time (seconds)')
plt.show()

'''
Question 4:
The graph depicting interpolation search performance with various initial midpoints shows a clear correlation between the choice of the initial midpoint and algorithm efficiency.
As the initial midpoint changes, execution times vary, indicating an impact on overall performance. 
This behavior resonates with that of an interpolation search, where the initial midpoint influences the algorithm's convergence speed.
Optimal performance is achieved by aligning the initial midpoint with the distribution of target values in the array, allowing for quicker convergence towards the target.
'''