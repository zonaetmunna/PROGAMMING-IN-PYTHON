import numpy as np
# rules of slicing: start:end:step
# The result includes the start index, but excludes the end index.
# Negative Slicing: Use the minus operator to refer to an index from the end:

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Slice elements from index 4 to the end of the array:
print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
print(arr[:4])

# Use the minus operator to refer to an index from the end:
print(arr[-3:-1])

# Return every other element from index 1 to index 5:
print(arr[1:5:2])

# Return every other element from the entire array:
print(arr[::2])

# Slicing 2-D Arrays
# From the second element, slice elements from index 1 to index 4 (not included):
arr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2d[1, 1:4])

# From both elements, return index 2:
print(arr2d[0:2, 2])
