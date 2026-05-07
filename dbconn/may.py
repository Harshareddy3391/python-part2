import mysql.connector



dbconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harsha@345",
    database="cls_may"
)


if dbconn.is_connected():
    print("connect successfully")
else:
    print("error")

cursor=dbconn.cursor()

create_table='''
create table employess(
id int primary key,
name varchar(30),
esal float ,
age int check(age>18),
gender varchar(30)

)
'''
#cursor.execute(create_table)

data='''
INSERT INTO employess(id, name, esal, age, gender)

VALUES(%s, %s, %s, %s, %s)

'''

val_data=[
     (1, "Harsha", 50000, 22, "Male"),
    (2, "Rahul", 45000, 25, "Male"),
    (3, "Priya", 55000, 24, "Female"),
    (4, "Anu", 60000, 26, "Female")
]

update='''
update employess set name="reddy" where id=1 '''

read='''
select * from employess'''


delate='''
DELETE FROM employess
WHERE id = 2'''


cursor.execute(delate)
#cursor.executemany(data,val_data)
cursor.execute(read)
 

rows = cursor.fetchall()

for i in rows:
    print(i)

dbconn.commit()

print('data inserted successfully')