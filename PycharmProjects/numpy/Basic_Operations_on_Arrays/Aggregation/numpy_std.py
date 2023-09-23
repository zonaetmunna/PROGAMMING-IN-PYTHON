import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Standard deviation of all elements
std_deviation = np.std(arr)

# Standard deviation along rows (axis=0)
row_std_deviation = np.std(arr, axis=0)

# Standard deviation along columns (axis=1)
col_std_deviation = np.std(arr, axis=1)

print(std_deviation)       # Output: 1.707825127659933
print(row_std_deviation)   # Output: [1.5 1.5 1.5]
print(col_std_deviation)   # Output: [0.81649658 0.81649658]
