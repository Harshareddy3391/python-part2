class Employee:
    def __init__(self,name,last,pay):
        self.name=name
        self.last=last
        self.pay=pay
        self.email=f"{name.lower()}.{last.lower()}@gmail.com"


    def full_name(self):
        self.full_name_=f"{self.name} {self.last}"
        return self.full_name_

e1=Employee("Harsha","Vardhan",100000)

print(e1.__dict__)
print(e1.full_name())