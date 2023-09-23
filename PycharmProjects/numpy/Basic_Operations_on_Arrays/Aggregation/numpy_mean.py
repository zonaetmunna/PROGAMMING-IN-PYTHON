import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Mean of all elements
average = np.mean(arr)

# Mean along rows (axis=0)
row_average = np.mean(arr, axis=0)

# Mean along columns (axis=1)
col_average = np.mean(arr, axis=1)

print(average)    # Output: 3.5
print(row_average)  # Output: [2.5 3.5 4.5]
print(col_average)  # Output: [2. 5.]
