from bs4 import BeautifulSoup
import requests
import pandas as pd

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary:$92,000,000</p><h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html?"
soup=BeautifulSoup(html, 'html5lib')

tag_object = soup.title
print(tag_object)

tag_object=soup.h3
print(tag_object)

tag_child = tag_object.b 
print(tag_child)

parent_tag = tag_child.parent
print(parent_tag)

sibling_1 = tag_object.next_sibling
print(sibling_1)

print(tag_child.attrs)


html1="<table><tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Lottle Caesars </td><td>12</td><td>144</td></table>"
table=BeautifulSoup(html1, 'html5lib')

table_row=table.find_all(name='tr')
print(table_row)

first_row = table_row[0]
print(first_row)

for i, row in enumerate(table_row):
    print('row', i)
    cells = row.find_all('td')

    for j, cell in enumerate(cells):
        print('column', j, 'cell', cell)

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')
#print(soup.prettify())

table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> \
<td>Payload mass</td></tr><tr> <td>1</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td> \
<td>300 kg</td></tr><tr><td>2</td> \
<td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td> \
<td>94 kg</td></tr><tr><td>3</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td> \
<td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')
table_rows = table_bs.find_all('tr')
print(table_rows)

first_row = table_rows[0]
print(first_row)

print(type(first_row))

print(first_row.td)

for i, row in enumerate(table_rows):
    print("row", i, "is", row)

list_input = table_bs.find_all(name=["tr", "td"])
#print(list_input)

print(table_bs.find_all(id="flight"))

list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)

print(table_bs.find_all('a', href=True))

print(table_bs.find_all('a', href=False))

print(soup.find_all(id="boldest"))

print(table_bs.find_all(string="Florida"))

two_tables="<h3>Rocket Launch </h3> \
<p><table class='rocket'> \
<tr><td>Flight No</td><td>Launch site</td><td>Payload mass</td></tr> \
<tr><td>1</td><td>Florida</td><td>300 kg</td></tr> \
<tr><td>2</td><td>Texas</td><td>94 kg</td></tr> \
<tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p>\
<p><h3>Pizza Party</h3> \
<table class='pizza'> \
<tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr> \
<tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr> \
<tr><td>Little Caesars</td><td>12</td><td >144 </td></tr> \
<tr><td>Papa John's</td><td>15 </td><td>165</td></tr>"

two_tables_bs = BeautifulSoup(two_tables, 'html.parser')

url = "http://www.ibm.com"
data = requests.get(url).text
soup = BeautifulSoup(data, "html5lib")  # create a soup object using the variable 'data'

for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

for link in soup.find_all('img'):  # in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))

# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"'

# get the contents of the webpage in text format and store in a variable called data
data = requests.get(url).text

soup = BeautifulSoup(data, "html5lib")

# find a html table in the web page
table = soup.find('table')  # in html table is represented by the tag <table>

# Get all rows from the table
for row in table.find_all('tr'):  # in html table row represented by tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td')  # in html a column is represented by tag <td>
    color_name = cols[2].string  # store the value in column 3 as color_name
    color_code = cols[3].text  # store the value in column 4 as color_code
    print("{}--->{}".format(color_name, color_code))

#Scraping tables from a Web page using Pandas
# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

tables = pd.read_html(url)
print(tables)

print(tables[0])

