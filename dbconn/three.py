import mysql.connector



conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harsha@345",
    database="python_db"
)


if conn.is_connected():
    print("database connection successfully")

else:
    print("connction fail")

cursor=conn.cursor()

sql_q='''
create table collage_data(
name varchar(32),
id int,
loc varchar(30)
)

'''
cursor.execute(sql_q)
head='''
insert into collage_data(name,id,loc) values(%s,%s,%s)

'''
data=[
      ("Vardhan", 101, "Hyderabad"),
    ("Raju", 102, "Bangalore"),
    ("Ram", 103, "Chennai")
]

cursor.executemany(head,data)


conn.commit()

print("created table and multiple records entered successfully...")


cursor.close()
conn.close()

 