import pandas as pd

# Read the CSV file into a DataFrame
#df = pd.read_csv('ex.csv')

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

print(s[2]) 

# Access the element at position 3 (value 40)
print(s.iloc[3]) 

# Access a range of elements by label
print(s[1:4])   

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

# Access the 'Name' column
print(df['Name'])  

# Access the third row by position
print(df.iloc[2])   

# Access the second row by label
print(df.loc[1])    

# Select specific columns
print(df[['Name', 'Age']])  

# Select specific rows
print(df[1:3])   

#Finding Unique Elements
unique_dates = df['Age'].unique()

#Conditional Filtering:
high_above_102 = df[df['Age'] > 25]

#Saving DataFrames
df.to_csv('trading_data.csv', index=False)
