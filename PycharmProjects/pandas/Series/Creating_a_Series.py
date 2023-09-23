import pandas as pd
import numpy as np

# Creating a Series from a list
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)

# Creating a Series from a NumPy array
data_array = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(data_array)

# Creating a Series from a dictionary
data_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
series_from_dict = pd.Series(data_dict)

print(series_from_list)
print(series_from_array)
print(series_from_dict)
