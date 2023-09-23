import pandas as pd

data_dict = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df_from_dict = pd.DataFrame(data_dict)

print(df_from_dict)
