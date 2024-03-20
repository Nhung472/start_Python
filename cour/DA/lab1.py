print('Hello, Python!')

print(bool(1))

#findall
import re
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
result = re.findall("as", s2)

print(result)

#serch
s1 = "Michael Jackson is the best"
pattern = r"Jackson"
result = re.search(pattern, s1)
if result:
    print("Match found!")
else:
    print("Match not found.")

#split
split_array = re.split("\s", s2)
print(split_array)

#sub
pattern = r"King of Pop"
replacement = "legend"
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
print(new_string) 

#In the string s3, find whether the digit is present or not using the \d and search() function:
s3 = "House number- 1105"
result = re.search("\d", s3)
if result:
    print("Digit found")
else:
    print("Digit not found.")

#strip()
my_string="Hello  " 
trimmed = my_string.strip()
print(my_string)

x=2/2
#x=x+1
print(type(x) )