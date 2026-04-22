from SA import S_Account
#from CA import C_Account

def many(obj):
    print(obj.__dict__)   # print object data


d = S_Account('vardhan', 80, 'ha@gmail.com', 101)
#k=C_Account('raju',6000,201,'raju@mail.com',10000)
many(d)