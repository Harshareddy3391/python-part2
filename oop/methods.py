"""class Methods:
    s=400
    def __init__(self,name):
        self.ur_name=name
    def normal_method(self):
        pass
    @classmethod
    def cls_method(cls):
        pass
    @staticmethod
    def static_method():
        pass

a1=Methods("harsha")
print(a1.__dict__)


"""

"""

class Student:
    def __init__(self,name):
        self.user_name=name
    def upname(self):
        self.user_name +=9

a1=Student(3)
a1.upname()

print(a1.__dict__)

 """
"""
class Student:
    def __init__(self, name):
        self.user_name = name

    def upname(self):
        self.user_name += 9   # correct variable


a1 = Student(3)
a1.upname()

print(a1.__dict__)"""




class Student:
    def __init__(self,marks):
        self.marks=marks

    def update(self):
        self.marks +=20

a1=Student(100)
a1.update()

print(a1.__dict__)