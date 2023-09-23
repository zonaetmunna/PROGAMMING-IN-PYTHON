import numpy as np

# create array and dimensional array
arr0 = np.array(42)
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arr5 = np.array([1, 2, 3, 4], ndmin=6)

print(arr0)
print(arr1)
print(arr2)
print(arr3)
# check which type dimension
print(arr5.ndim)