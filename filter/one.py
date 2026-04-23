lst=["harsha","vardhan","harish","karthik","kiran"]


def new_data(data):

    return data.startswith('h')

f_data=list(filter(new_data,lst))


print(f_data)