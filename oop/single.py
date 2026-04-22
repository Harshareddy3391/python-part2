class Student:

    def __init__(self):
        self.name="vardhan"



class Student1(Student):

    def m1(self):
        self.val=self.name



a=Student1()
a.m1()

print(a)