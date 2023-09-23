import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
print(x)

# where value is even
y = np.where(arr%2 == 0)
print(y)