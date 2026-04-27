import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harsha@345",
    database="python_db"
)


if conn.is_connected():
    print("connection success")
else:
    print("connection fail")


cursor = conn.cursor()

read_data='''
select id,name from users_data

'''
cursor.execute(read_data)
data=cursor.fetchall()

for i in data:
    print(i)

conn.commit()

cursor.close()
conn.close()
