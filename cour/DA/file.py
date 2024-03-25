#import piplite
import pandas as pd
import urllib.request
import numpy as np
import json
import urllib.request
import xml.etree.ElementTree as ET
from PIL import Image 
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
filename = 'addresses.csv'
urllib.request.urlretrieve(url, filename)

df = pd.read_csv("addresses.csv", header=None)

print(df)

df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
print(df)

print(df["First Name"])

df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
print(df)

# To select the first row
print(df.loc[0])

# To select the 0th,1st and 2nd row of "First Name" column only
print(df.loc[[0,1,2], "First Name" ])

# To select the 0th,1st and 2nd row of "First Name" column only
print(df.iloc[[0,1,2], 0])

#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

#applying the transform function
df = df.transform(func = lambda x : x + 10)
print(df)

result = df.transform(func = ['sqrt'])
print(result)

#JSON file Format
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

# Serializing json  
json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

print(json_object)

# Opening JSON file 
with open('sample.json', 'r') as openfile: 
    # Reading from json file 
    json_object = json.load(openfile) 
print(json_object) 
print(type(json_object)) 

#XLSX file format
#df = urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx")
#df = pd.read_excel("file_example_XLSX_10.xlsx")

#print(df)

#writting with xml.etree.elementtree
# create the file structure
#employee = ET.Element('employee')
#details = ET.SubElement(employee, 'details')
#first = ET.SubElement(details, 'firstname')
#second = ET.SubElement(details, 'lastname')
#third = ET.SubElement(details, 'age')
#first.text = 'Shiv'
#second.text = 'Mishra'
#third.text = '23'

# create a new XML file with the results
#mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
#with open("new_sample.xml", "wb") as files:
#    mydata1.write(files)

#!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml

#tree = etree.parse("Sample-employee-XML-file.xml")

#root = tree.getroot()
#columns = ["firstname", "lastname", "title", "division", "building","room"]

#datatframe = pd.DataFrame(columns = columns)
#for node in root: 
#    firstname = node.find("firstname").text
#    lastname = node.find("lastname").text 
#    title = node.find("title").text 
#    division = node.find("division").text 
#    building = node.find("building").text
#    room = node.find("room").text
#    datatframe = pd.concat([datatframe, pd.Series([firstname, lastname, title, division, building, room], index = columns)], ignore_index = True)

# Herein xpath we mention the set of xml nodes to be considered for migrating  to the dataframe which in this case is details node under employees.
#df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 

#datatframe.to_csv("employee.csv", index=False)

urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")
# Read image 
img = Image.open('./dog.jpg','r') 
# Output Images 
#img.show()

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
filename = 'diabetes.csv'
urllib.request.urlretrieve(url, filename)
df = pd.read_csv("diabetes.csv", header=None)

print(df)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe", df.head(5)) 

print(df.shape)

print(df.info())

print(df.describe())

missing_data = df.isnull()
print(missing_data.head(5))

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    

print(df.dtypes)

#Visualization
labels= 'Not Diabetic','Diabetic'
print(plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%'))
print(plt.legend())
print(plt.show())


