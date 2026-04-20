#class is user defined data type  in oop thats act as a bluprint for creating object
class Account:
    name="harsha"
    def Account_open(self):
        print("your account is opened")


    def Amount_deposit(self):
        print("amount is deposited")

a1=Account()
d=a1.Account_open()
s=a1.Amount_deposit()
print(a1.name)
 