import csv,os,requests,mysql.connector



#extract data
p_resp=requests.get('https://dummyjson.com/products')
p_data=p_resp.json()
products_data=p_data['products']



#TRANSFORM DATA
beauty_products=[]
beauty_products_json_formate=[]

for product in products_data:
    if product['category'] == "beauty":
        beauty_products.append((
            product['id'],
            product['title'],
            product['price'],
            product['rating'],
        ))
        beauty_products_json_formate.append({
            "id": product['id'],
            "title":product['title'],
            "price":product['price'],
            "rating":product['rating']

        })


#load data into csv file
if os.path.exists("data.csv"):
    with open("data.csv","w",newline="") as file1:
        write=csv.writer(file1)
        write.writerow(("id","titile",'price',"rating"))

        print("new csv file created susceefull...")
else:
    print("file created already..")


#load data into sql db

try:

    dbconn=mysql.connector.connect(
    host='localhost',user="root",password="Harsha@345",database="jul10"
    )
    cursor=dbconn.cursor()
    sql_st="""
    insert into products(id,name,price,rating)values(%s,%s,%s,%s);"""
    cursor.executemany(sql_st,beauty_products)
    dbconn.commit()
    print("data inserted into database...")
except Exception as e:
    print("hel")

finally:
    cursor.close()
    dbconn.close()
