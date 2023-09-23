import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate along axis 0 (rows)
concatenated_rows = np.concatenate((arr1, arr2), axis=0)

# Concatenate along axis 1 (columns)
concatenated_columns = np.concatenate((arr1, arr2), axis=1)  # Raises an error for 1D arrays

print(concatenated_rows)
print(concatenated_columns)
