import pandas as pd
import numpy as np

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
print(df)

ages = df['Age']
print(ages)

name_age = df[['Name', 'Age']]
print(name_age)

adults = df[df['Age'] > 30]
print(adults)

df_filled = df.fillna(0)
df_dropped = df.dropna()

# Define a dictionary with lists of different lengths
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a DataFrame using from_dict with orient='index'
df = pd.DataFrame.from_dict(data, orient='index').transpose()
print(df)

max_length = max(len(data[key]) for key in data)
for key in data:
    data[key] += [np.nan] * (max_length - len(data[key]))
df = pd.DataFrame(data)
print(df)