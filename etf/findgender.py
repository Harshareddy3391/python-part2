import json 


with open("new_json.json","r") as data:

    readdata=json.read(data)


    print(readdata)