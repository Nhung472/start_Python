#import piplite
#await piplite.install(['xlrd','openpyxl'])
#import pyodide_http
#from pyodide_http import pyfetch
import pandas as pd
import urllib.request

# Read data from CSV file

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
df = pd.read_csv(filename)

print(df)

print(df.head())

# Read data from Excel File and print the first five rows
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'
df = pd.read_excel(xlsx_path)
print(df.head())

# Access to the column Length
x = df[['Length']]
print(x)

# Get the column as a series
x = df['Length']
print(x)

# Get the column as a dataframe
x = df[['Artist']]
print(type(x))

# Access to multiple columns
y = df[['Artist','Length','Genre']]
print(y)

# Access the value on the first row and the first column
print(df.iloc[0, 0])

# Access the value on the second row and the first column
print(df.iloc[1,0])

# Access the value on the first row and the third column
print(df.iloc[0,2])

# Access the value on the second row and the third column
print(df.iloc[1,2])

# Access the column using the name
print(df.loc[1, 'Artist'])

# Slicing the dataframe
print(df.iloc[0:2, 0:3])

# Slicing the dataframe using name
print(df.loc[0:2, 'Artist':'Released'])

q = df[['Rating']]
print(q)

new_index=['a','b','c','d','e','f','g','h']
df_new=df
df_new.index=new_index
df_new.loc['a', 'Artist']
df_new.loc['a':'d', 'Artist']

