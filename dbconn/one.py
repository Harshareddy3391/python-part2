import mysql.connector


connction=mysql.connector.connect(host="localhost",user="root",password="Harsha@345")



if connction.is_connected :

    print("conncted successfully")


else:
    print("fail")

