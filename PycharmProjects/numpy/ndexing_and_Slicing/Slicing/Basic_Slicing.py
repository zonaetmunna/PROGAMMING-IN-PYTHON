import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing to get a portion of the array
subset1 = arr[2:6]   # [2, 3, 4, 5]
subset2 = arr[:5]    # [0, 1, 2, 3, 4]
subset3 = arr[::2]   # [0, 2, 4, 6, 8]

print(subset1)
print(subset2)
