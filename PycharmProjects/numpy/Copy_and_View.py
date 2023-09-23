'''
Copy:
A copy of an array is a completely separate object with its own data.
Modifying a copy does not affect the original array.
Copies are created explicitly using functions like np.copy() or by slicing an array with the copy() method.

View:
A view of an array is a new array that refers to the same data in memory as the original array. It is essentially a "window" into the data.
Modifications made to a view affect the original array.
Views are created implicitly by slicing or selecting elements from an array.
'''

import numpy as np

original_array = np.array([1, 2, 3, 4, 5])
copied_array = np.copy(original_array)
copied_array[0] = 99

print(original_array)  # Output: [1 2 3 4 5]
print(copied_array)    # Output: [99  2  3  4  5]
view_array = original_array[1:4]
view_array[0] = 99

print(view_array)      # Output: [99  3  4]