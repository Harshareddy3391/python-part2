class Employee:
    n=12
    def __init__(self,name,last,pay):
        self.name=name
        self.last=last
        self.pay=pay
        self.email=f"{name.lower()}.{last.lower()}@gmail.com"


    def full_name(self):
        self.full_name_=f"{self.name} {self.last}"
        return self.full_name_
    def inc(self,p):
        self.pay+=int(self.pay * 20/100)

e1=Employee("Harsha","Vardhan",100000)
print(e1.inc(20))
e1.pa=21
print(e1.__dict__)
print(e1.full_name())
print(Employee.n)
 