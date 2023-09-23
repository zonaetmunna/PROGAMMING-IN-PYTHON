import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 28, 22],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']}
df = pd.DataFrame(data)

# Select a single column
names = df['Name']

# Select multiple columns
name_and_age = df[['Name', 'Age']]

print(names)
print(name_and_age)