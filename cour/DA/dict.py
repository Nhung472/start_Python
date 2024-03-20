Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)

print(Dict["key1"])

# Access to the value by the key
print(Dict[(0, 1)])

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)

# Get value by keys
print(release_year_dict['Thriller'] )
print(release_year_dict['The Bodyguard'] )

print(release_year_dict.keys() )
print(release_year_dict.values() )

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
print(release_year_dict)

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print(release_year_dict)

'The Bodyguard' in release_year_dict


#create
dic = {}

#Store the first product details in variable
ProductName1 = "Mobile phone"
ProductQuantity1 = 5
Productprice1 = 20000
ProductReleaseYear1 = 2020

#Add the details in list
dic["ProductName1"] = ProductName1
dic["ProductQuantity1"] = ProductQuantity1
dic["Productprice1"] = Productprice1
dic["ProductReleaseYear1"] = ProductReleaseYear1

#Store the second product details in a variable
ProductName2 = "Laptop"
ProductQuantity2 = 10
Productprice2 = 50000
ProductReleaseYear2 = 2023

dic["ProductName2"] = ProductName2
dic["ProductQuantity2"] = ProductQuantity2
dic["Productprice2"] = Productprice2
dic["ProductReleaseYear2"] = ProductReleaseYear2

print("ProductReleaseYear2" in dic)
print("ProductReleaseYear1" in dic)

#Delete release year of both the products from the inventory
del(dic["ProductReleaseYear1"])
del(dic["ProductReleaseYear2"])


print(dic)

Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
print(Dict["D"])
