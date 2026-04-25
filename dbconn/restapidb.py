import requests




responce=requests.get("https://jsonplaceholder.typicode.com/users")

json_data=responce.json()

lst_data=[]

for i in json_data:
    lst_data.append((i['id'],i['name'],i['address']['zipcode'],i['phone'],i['email']))


f=lambda x: x 

print(f(lst_data))

 


