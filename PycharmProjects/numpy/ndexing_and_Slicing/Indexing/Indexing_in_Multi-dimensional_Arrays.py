import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Accessing individual elements
element_00 = arr[0, 0]  # Access the element in the first row and first column (1)
element_21 = arr[2, 1]  # Access the element in the third row and second column (8)

print(element_00)
print(element_21)
