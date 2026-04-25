import json
import mysql.connector



with open("one.json","r") as data:
    data_read=json.load(data)

empt_lst=[]


for i in data_read:
     
    empt_lst.append((i['id'],i['first_name'],i['last_name'],i['gender']))


print("data opened successfully list formate.....")


dbconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harsha@345",
    database="python_db"
)


if dbconn.is_connected():
    print("database conncted successfully... ")
else:
    print("connction fail..")


cursor=dbconn.cursor()

table='''
create table json_data(
id int,
f_name varchar(32),
l_name varchar(30),
gender varchar(30)

) 

'''

cursor.execute(table)

table_column='''
insert into json_data(id,f_name,l_name,gender) values (%s,%s,%s,%s)

'''
cursor.executemany(table_column,empt_lst)


dbconn.commit()

print("data inserted successfully multiple records....")

cursor.close()
dbconn.close()