import pandas as pd


# data = pd.read_csv("music_test.csv")
# print(data) # print all rows


# print(data.head()) # print top 5 rows
# print(data.describe()) #perform mathematical operations on table
# df = data
# print(df["Age"])


'''
Pandas is a powerful Python library used for data manipulation and analysis.It provides data structures and functions for efficiently handling structured data.
Here's a brief overview of some key components and functionalities:

1. DataFrame:
DataFrame is the primary data structure in pandas. It represents data in a tabular format similar to a spreadsheet or SQL table.
It consists of rows and columns, where each column can have a different data type (e.g., integers, floats, strings).
You can create a DataFrame from various data sources like CSV files, Excel files, SQL databases, or even from Python dictionaries.

2. Series:
Series is a one-dimensional labeled array capable of holding data of any type (integers, strings, floats, Python objects, etc.).
It's similar to a column in a DataFrame.

3.Data Selection and Manipulation:
Pandas provides powerful methods to select, filter, and manipulate data. You can access specific rows, columns, or individual elements using labels or indices.
Operations like merging, joining, grouping, sorting, and reshaping data are straightforward in pandas.

4. Data Input/Output:
Pandas supports reading and writing data from/to various file formats such as CSV, Excel, JSON, SQL databases, and more.
For instance, pd.read_csv() and df.to_csv() are used to read and write CSV files, respectively.
Data Cleaning:

Pandas offers a wide range of functions to handle missing data, duplicate data, and data type conversion.
Methods like dropna(), fillna(), and astype() are commonly used for cleaning data.

5. Data Visualization:
Although pandas itself doesn't have visualization capabilities, it integrates well with libraries like Matplotlib and Seaborn for data visualization.
You can create plots directly from pandas objects using .plot() method.

6. Time Series Data:
Pandas provides robust support for working with time series data, including functionalities like date range generation, shifting, resampling, and rolling window operations.

7. Performance:
Pandas is highly optimized for performance. However, it's often recommended to be careful with memory usage and to use vectorized operations whenever possible for better performance.
Pandas is widely used in data analysis, data cleaning, data transformation, and data visualization tasks in various fields like finance, economics, scientific research, and more. 
Its ease of use and flexibility make it a go-to tool for many data professionals and researchers.
'''


'''
Certainly! Pandas offers a wide range of methods to manipulate, analyze, and transform data in DataFrames and Series. Here's an overview of some commonly used methods:

DataFrame Methods:
Creation and Loading:
pd.DataFrame(): Create a DataFrame from lists, dictionaries, or other data structures.
pd.read_csv(), pd.read_excel(), pd.read_sql(): Load data from CSV, Excel, SQL databases, etc.
'''

print(" Cration of Dataframe from list")
l1 = [[101, "shraddha"], [102, "Sourabh"], [103, "Dodo"], [104, "Golu"]]
df = pd.DataFrame(l1)
print(df)

'''
Exploration:
.head(), .tail(): View the first or last few rows of the DataFrame.
.info(): Get concise summary of the DataFrame including data types and missing values.
.describe(): Generate descriptive statistics (count, mean, std, min, max, etc.) of numerical columns.
.shape, .size: Get the dimensions and total number of elements in the DataFrame.
'''

print(df.head())
print(df.info())
print(df.info())
print(df.shape)
print(df.size)


'''
Indexing and Selection:
.loc[], .iloc[]: Select rows and columns by label or integer-location.
.at[], .iat[]: Fast scalar access using label or integer-location.
'''

print(df.loc[0][1]) #return element
print(df.loc[1]) #return row
print("he,lllooo", df.iloc[1]) # print 
print()


'''
Data Manipulation:
.copy(): Create a copy of the DataFrame.
.drop(): Drop specified labels (rows or columns).
.dropna(), .fillna(): Drop or fill missing values.
.replace(): Replace values.
.rename(): Rename index or column labels.
.astype(): Cast the DataFrame to a specified dtype.
'''

df1 = df.copy()
print(df1)

df1 = df1.drop([3])
print(df1)


'''
Aggregation and Grouping:
.groupby(): Group DataFrame using a mapper or by a Series of columns.
.agg(), .aggregate(): Aggregate using one or more operations over the specified axis.
.pivot_table(): Create a pivot table.

Sorting and Ranking:
.sort_values(): Sort by the values along either axis.
.sort_index(): Sort object by labels along the given axis.
.rank(): Compute numerical data ranks.

Combining Data:
.merge(), .join(): Merge or join DataFrame objects.
.concat(): Concatenate pandas objects along a particular axis.

Time Series:
.resample(): Resample time-series data.
.rolling(): Provide rolling window calculations.

Plotting and Visualization:
.plot(): Plot data.
.hist(), .boxplot(), .scatter(): Plot histograms, boxplots, scatter plots, etc.
Series Methods:
'''
import matplotlib.pyplot as plt

# Create a DataFrame
data = {'x': range(10), 'y': [i**2 for i in range(10)]}
df = pd.DataFrame(data)

# Plot a line plot
df.plot(x='x', y='y', figsize=(8, 6))
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Plotting a basic histogram
plt.hist(df, bins=30, edgecolor='black')
# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Basic Histogram')
# Display the plot
plt.show()

'''
Indexing and Selection:
.loc[], .iloc[]: Select items by label or integer-location.
.at[], .iat[]: Access a single value for a row/column label pair or integer-location pair.

Operations:
.add(), .sub(), .mul(), .div(): Perform element-wise addition, subtraction, multiplication, division.
.apply(), .map(): Apply a function to each element.
.value_counts(): Count distinct values.

Data Handling:
.drop_duplicates(): Remove duplicate values.
.dropna(), .fillna(): Drop or fill missing values.

Aggregation:
.sum(), .mean(), .min(), .max(): Calculate sum, mean, min, max, etc.
.count(): Count non-NA/null values.
.std(), .var(): Compute standard deviation and variance.

Time Series:
.shift(): Shift index by desired number of periods.
.diff(): Compute the difference of a Series element compared with another element in the Series.
These are just some of the most commonly used methods in Pandas. The library is quite extensive and flexible, allowing for a wide range of data manipulation and analysis tasks.

'''