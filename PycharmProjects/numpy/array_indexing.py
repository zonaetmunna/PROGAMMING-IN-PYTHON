import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
# second element
print(arr[1])
# third and fourth elements summation
print(arr[2] + arr[3])

# Access the element on the first row, second column:
arr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st row: ', arr2d[0, 1])
# Access the element on the 2nd row, 5th column:
print('5th element on 2nd row: ', arr2d[1, 4])
