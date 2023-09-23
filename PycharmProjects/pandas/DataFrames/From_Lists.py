import pandas as pd

# Creating a DataFrame from a list of lists
data_list = [
    [1, 'Alice', 25],
    [2, 'Bob', 30],
    [3, 'Charlie', 35]
]
columns = ['ID', 'Name', 'Age']
df_from_list = pd.DataFrame(data_list, columns=columns)

# Creating a DataFrame from a list of dictionaries
data_dict = [
    {'ID': 1, 'Name': 'Alice', 'Age': 25},
    {'ID': 2, 'Name': 'Bob', 'Age': 30},
    {'ID': 3, 'Name': 'Charlie', 'Age': 35}
]
df_from_dict = pd.DataFrame(data_dict)

print(df_from_list)
print(df_from_dict)
