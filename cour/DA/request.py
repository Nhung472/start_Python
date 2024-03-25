import requests
import os 
from PIL import Image
from IPython.display import IFrame
from randomuser import RandomUser
import pandas as pd
import json

url = 'http://www.ibm.com/'
r=requests.get(url)
print(r.status_code)

print(r.request.headers)

print("request body:", r.request.body)

header = r.headers
print(header)

print(header['date'])

print(header['Content-Type'])

print(r.encoding)

print(r.text)

print(r.text[0:100])

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)
print(r.headers)

r.headers['Content-Type']

path=os.path.join(os.getcwd(),'image.png')

with open(path,'wb') as f:
    f.write(r.content)

print(Image.open(path))

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)

url_get='http://httpbin.org/get'

payload={"name":"Joseph","ID":"123"}

r=requests.get(url_get,params=payload)

print(r.url)
print(r.json()['args'])

#Post Requests
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

r_post.json()['form']

r = RandomUser()
some_list = r.generate_users(10)
print(some_list)

name = r.get_full_name()

for user in some_list:
    print (user.get_full_name()," ",user.get_email())

for user in some_list:
    print (user.get_picture())

def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

print(get_users())

df1 = pd.DataFrame(get_users())  
data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
print(pd.DataFrame(results))

df2 = pd.json_normalize(results)
print(df2)

cherry = df2.loc[df2["name"] == 'Cherry']
print((cherry.iloc[0]['family']) , (cherry.iloc[0]['genus']))

cal_banana = df2.loc[df2["name"] == 'Banana']
print(cal_banana.iloc[0]['nutritions.calories'])

data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")
results2 = json.loads(data2.text)
df3 = pd.DataFrame(results2)
df3.drop(columns=["type","id"],inplace=True)
print(df3)

