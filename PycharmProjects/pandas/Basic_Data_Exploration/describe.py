import pandas as pd

# Create a sample DataFrame
data = {'Age': [25, 30, 35, 28, 22]}
df = pd.DataFrame(data)

# Generate summary statistics
summary = df.describe()

print(summary)
