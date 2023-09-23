import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Slicing to extract subArrays
subarray1 = arr[0:2, 1:3]
subarray2 = arr[:, 1]  # Slicing a specific column

print(subarray1)
print(subarray2)
