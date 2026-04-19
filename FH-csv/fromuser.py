import csv

fp=open('user.csv','w',newline="")

userdata=csv.writer(fp)
userdata.writerow(['id','name','sal'])
 

n=int(input("enter no.of rows"))

for i in range(n):
    id=input("enter id")
    name=input("enter name")
    sal=input("enter sal")
    userdata.writerow(['id','name','sal'])
 

fp.close()