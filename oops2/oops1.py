def create_emp(first,last,pay):
    email=f"{first.lower()}.{last.lower()}@infosys.com"
    return {"first":first,"last":last,"email":email,"pay":pay}


def incr_sal(emp,pers):
    emp["pay"]=int(emp["pay"]*(1+pers/100))

emp1=create_emp("rahul","sharma",3000)
print(emp1)
salinc=incr_sal(emp1,50)
print(salinc)
"""
emp1_first="Rahul"
emp1_last="sharma"
emp1_email="sharma@info.gmail"

emp2_first="punith"
emp2_last="raj"
emp2_email="raj@info.gmail"""