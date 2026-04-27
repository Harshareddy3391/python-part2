import requests,mysql.connector




responce=requests.get("https://jsonplaceholder.typicode.com/users")

json_data=responce.json()

lst_data=[]

for i in json_data:
    lst_data.append((i['id'],i['name'],i['address']['zipcode'],i['phone'],i['email']))

 
print("json fetched from the rest api siccessfully....")



conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harsha@345",
    database="python_db"
)



if conn.is_connected():
    ("your database connected successfully.......")



else:
    print("connction fail....")


cursor=conn.cursor()

create_tb='''
create table users_data (
id int,
name varchar(30),
zip_code varchar(30),
phone varchar(30),
email varchar(90)

)

'''

cursor.execute(create_tb)

print("table is created sucessfully...")

tb_column='''
insert into users_data(id,name,zip_code,phone,email) values (%s,%s,%s,%s,%s)
'''

cursor.executemany(tb_column,lst_data)


conn.commit()

print("data inserted successfully...")


cursor.close()
conn.close()



 


