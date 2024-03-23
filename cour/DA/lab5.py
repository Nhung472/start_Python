import pandas as pd

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
print(x)

print(type(x))

#Retrieving the Department, Salary and ID columns and assigning it to a variable z
z = df[['Department','Salary','ID']]
print(z)

y = {'Student': ['David', 'Samuel', 'Terry', 'Evan'], 
     'Age': [27, 24, 22, 32], 
     'Country': ["UK", 'Canada', 'China', 'USA'],
    'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
    'Marks': [85, 72, 89, 76]}

df1 = pd.DataFrame(y)
print(df1)

b = df1[['Marks']]
print(b)

c = df1[['Country','Course']]
print(c)

# Access the value on the first row and the first column
print(df.iloc[0, 0])

# Access the value on the first row and the third column
print(df.iloc[0,2])

# Access the column using the name
print(df.loc[0, 'Salary'])

df2=df
df2=df2.set_index("Name")

print(df2.head())

#Now, let us access the column using the name
print(df2.loc['Jane', 'Salary'])

print(df2.loc['Jane', 'Department'])

print(df2.iloc[3, 2])

# let us do the slicing using old dataframe df
print(df.iloc[0:2, 0:3])

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
print(df.loc[0:2,'ID':'Department'])

#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
print(df2.loc['Rose':'Jane', 'ID':'Department'])

