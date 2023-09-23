import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Fancy indexing with an array of indices
indices = np.array([1, 3])
selected_elements = arr[indices]

print(selected_elements)  # Output: [20, 40]
