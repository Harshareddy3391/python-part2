import json


with open('data.json','r',newline="") as a:

    dataread=json.load(a)

    for i in dataread:

        print(i['email'])
        print(i['email'])


