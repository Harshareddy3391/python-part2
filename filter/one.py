lst=["harsha","vardhan","harish","karthik","kiran"]
"""

def new_data(data):

    return data.startswith('h')

f_data=list(filter(new_data,lst))

"""

f_data=list(filter(lambda verify: verify.endswith('n'),lst))
print(f_data)