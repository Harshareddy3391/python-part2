import csv,os,requests



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
    with open("data.csv","w",newline=" ") is file1:
        write=csv.writer(file1)
        write.writerow("id","titile",'price',"rating")

print("new csv file created susceefull...")


