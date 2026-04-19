import csv

with open('emp.csv','r') as fp:

    da=csv.reader(fp)
    lst=list(da)

    for i in lst:
        print(i[2])


    print(type(da))
   
    fp.close