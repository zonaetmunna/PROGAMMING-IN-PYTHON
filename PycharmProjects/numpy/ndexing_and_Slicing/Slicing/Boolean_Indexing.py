import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Boolean indexing to filter elements greater than 3
filtered_array = arr[arr > 3]

print(filtered_array)  # Output: [4, 5]
