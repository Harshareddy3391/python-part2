import json 


with open("new_json.json","r") as data:

    readdata=json.load(data)

    m_data=filter(lambda da:da["gender"] == "Male",readdata)
    f_data=filter(lambda da:da["gender"] == "Female",readdata)




    print("total males :",len(list(m_data)))
    print("total males :",len(list(f_data)))
    print(len(readdata))

