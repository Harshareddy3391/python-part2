class Employee:
    def __init__(self,name,last,pay):
        self.name=name
        self.last=last
        self.pay=pay
        self.email=f"{name.lower()}.{last.lower()}@gmail.com"

e1=Employee("Harsha","Vardhan",100000)

print(e1.__dict__)