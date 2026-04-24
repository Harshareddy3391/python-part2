#invoke the rest api and write the data in json file

#work with requist module

import requests

"""
usage : featch all users
Rest API URL : https://dummyjson.com/users
method type : GET 
Required fields : None
Access type : Public
"""



data=requests.get('https://dummyjson.com/users')

print(data)