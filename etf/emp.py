import csv
import json


with open('empdata.csv','r') as fp:


    data=csv.reader(fp)
    lst_data=list(data)
    rem_cl_data=lst_data[1:]


emt_arry=[]
for i in rem_cl_data:

    emt_arry.append({
        "id":i[0],
        "username":i[1].upper(),
        "email":i[2],
        "gender":i[3],
        "city":"india"
        
        })



with open("new_json.json","w") as fp2:
    json.dump(emt_arry,fp2)


print("new file will be created")