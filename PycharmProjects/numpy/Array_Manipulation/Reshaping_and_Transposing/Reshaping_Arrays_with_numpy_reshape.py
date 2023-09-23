import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])  # 1D array with 6 elements

# Reshaping to a 2D array with 2 rows and 3 columns
reshaped_arr = np.reshape(arr, (2, 3))

print(reshaped_arr)
