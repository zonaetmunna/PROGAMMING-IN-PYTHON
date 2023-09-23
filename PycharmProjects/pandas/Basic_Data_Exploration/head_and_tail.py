import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 28, 22]}
df = pd.DataFrame(data)

# Display the first 3 rows
print(df.head(3))
