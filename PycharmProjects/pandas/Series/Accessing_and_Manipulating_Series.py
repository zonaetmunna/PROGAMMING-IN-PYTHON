import pandas as pd

# Creating a Series from a list
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)

# Creating a Series from a dictionary
data_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
series_from_dict = pd.Series(data_dict)


# Accessing elements by index
print(series_from_list[0])  # Access the first element
print(series_from_dict['B'])  # Access the element with label 'B'

# Slicing the Series
print(series_from_list[1:4])  # Slice from index 1 to 3 (exclusive)

# Performing arithmetic operations
result = series_from_list * 2  # Multiply all elements by 2
print(result)

# Filtering elements
filtered_series = series_from_dict[series_from_dict > 20]
print(filtered_series)


print(series_from_list.index)  # Index labels
print(series_from_list.values)  # Data values as a NumPy array
print(series_from_list.dtype)   # Data type of elements in the Series
