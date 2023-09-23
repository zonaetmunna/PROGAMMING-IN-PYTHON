import numpy as np
# By default Python have these data types: strings, integer, float, boolean, complex
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''


arr = np.array([1, 2, 3, 4])

# The NumPy array object has a property called dtype that returns the data type of the array:
print(arr.dtype)

# Get the data type of an array containing strings:
arrSting = np.array(['apple', 'banana', 'cherry'])
print(arrSting.dtype)

# Create an array with data type string:
arrstring2=np.array([1, 2, 3, 4], dtype='S')
print(arrstring2.dtype)

