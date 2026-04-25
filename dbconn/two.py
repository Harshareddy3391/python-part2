import mysql.connector


con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harsha@345",
    database="python_db"

)



if con.is_connected() :
    print("successfully created connction....")

else:
    print("connction fail")


cursor=con.cursor()

quary='''
create table student(
name varchar(32),
id int,
location varchar(40)

)

'''

head='''
INSERT INTO student (name,id,location) VALUES (%s,%s,%s)

'''

data = [
    ("Vardhan", 101, "Hyderabad"),
    ("Raju", 102, "Bangalore"),
    ("Ram", 103, "Chennai")
]
cursor.executemany(head,data)

con.commit()

print("second table also cretead successfully")


cursor.close()
con.close()