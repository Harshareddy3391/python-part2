from Account import Account


class C_Account(Account):

    bal=400

    def __init__(self, name, amount,id,email,val):
        super().__init__(name, amount)



        self.id=id
    
        self.mail=email
        self.val=val


    def cal_bal(self):
            print(self.val - self.bal)

    

"""

s=C_Account('raju',6000,201,'raju@mail.com',10000)

s.cal_bal()
 
#print(s.cal_bal())
print(s.__dict__)"""


