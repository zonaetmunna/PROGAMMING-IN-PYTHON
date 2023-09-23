import pandas as pd

# Create a sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
        'Age': [25, 30, None, 28, 22]}
df = pd.DataFrame(data)

# Display information about the DataFrame
df.info()
