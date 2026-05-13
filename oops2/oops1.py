def create_emp(first,last,pay):
    email=f"{first.lower()}.{last.lower()}@infosys.com"
    return {"first":first,"last":last,"email":email,"pay":pay}

emp1=create_emp("rahul","sharma",3000)
print(emp1)

emp1_first="Rahul"
emp1_last="sharma"
emp1_email="sharma@info.gmail"

emp2_first="punith"
emp2_last="raj"
emp2_email="raj@info.gmail"