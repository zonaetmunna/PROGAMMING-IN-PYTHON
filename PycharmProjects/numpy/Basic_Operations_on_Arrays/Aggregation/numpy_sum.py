import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Sum of all elements
total_sum = np.sum(arr)

# Sum along rows (axis=0)
row_sum = np.sum(arr, axis=0)

# Sum along columns (axis=1)
col_sum = np.sum(arr, axis=1)

print(total_sum)  # Output: 21
print(row_sum)    # Output: [5 7 9]
print(col_sum)    # Output: [ 6 15]
