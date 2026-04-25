import mysql.connector


connction=mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="Harsha@345",
                                  database="python_db"
                                  )



if connction.is_connected :

    print("conncted successfully")


else:
    print("fail")



cursor=connction.cursor()

sql_statement='''
 create table employee(
 name varcar(32),
 id int,
 sal float
 
 
 );

'''

