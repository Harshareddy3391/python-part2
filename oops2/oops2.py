class Employee:

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=f"{first.lower()}.{last.lower()}@gmail.com"


    def full_name(self):
        return f"{self.first}{self.last}"




    #pass


emp1=Employee("Rahul","sharma",5000)
emp2=Employee("raj","put",30)
emp1.pay=300
print(emp1.__dict__)
print(emp2.__dict__)
print(emp1.full_name())