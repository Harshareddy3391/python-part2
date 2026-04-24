#invoke the rest api and write the data in json file

#work with requist module

import requests,json

"""
usage : featch all users
Rest API URL : https://dummyjson.com/users
method type : GET 
Required fields : None
Access type : Public
"""



dataa=requests.get('https://dummyjson.com/users')
status_data=dataa.status_code
json_data=dataa.json()
emt_list=[]
for i in json_data["users"]:
    emt_list.append({
        "id":i['id'],
        "first_name":i["firstName"],
        "gender":i['gender'],
        "age":i["age"],
        "lastName":i['lastName'],
        "email":i["email"]

        })
      

with open("using_re.json","w") as data:
    json.dump(emt_list,data,indent=8)


    print("new fill will be created successfully")
"""
print("hello")

print(data)
print(status_data)
for i in json_data['users']:
    pass"""