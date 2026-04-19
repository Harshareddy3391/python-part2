import csv

fp = open('writedata.csv', 'w', newline='')  # ✅ add newline=''

data = csv.writer(fp)

# ✅ each field as separate string
data.writerow(["id", "first_name", "last_name", "email", "gender", "ip_address"])
data.writerow(["1", "Eba", "Hammerson", "ehammerson0@guardian.co.uk", "Female", "39.108.179.177"])

fp.close()  # ✅ added ()

# ✅ print inside the with block
with open('writedata.csv', 'r') as a:
    readdata = csv.reader(a)
    for i in readdata:
        print(list(i))

    print(list(readdata))
   
     # ✅ iterate to print rows
 
# no need to call a.close() — 'with' handles it automatically ✅