from Account import Account


class S_Account(Account):


    def __init__(self, name, amount,mail,id):

       # self.name_user=name
        #self.amount_user=amount
        
        super().__init__(name, amount)

        self.mail_user=mail
        self.id_user=id

"""

S=S_Account('vardhan',80,'ha@gmail.com',101)
print(S.__dict__)"""