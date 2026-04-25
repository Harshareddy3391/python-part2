import mysql.connector


connction=mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="Harsha@345",
                                  database="python_db"
                                  )



if connction.is_connected() :

    print("conncted successfully")


else:
    print("fail")



cursor=connction.cursor()

sql_statement='''
 create table employee(
 name varchar(32),
 id int,
 sal float
 
 
 );

'''


cursor.execute(sql_statement)
connction.commit()

print("table is created successfully")

 
cursor.close()

connction.close()