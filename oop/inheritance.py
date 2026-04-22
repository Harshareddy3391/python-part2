class Student:

    def __init__(self):
        self.name_user="HARSHA"

class Student1(Student):

    def __init__(self):
        super().__init__()



s=Student1()

print(s.__dict__)