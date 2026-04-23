lst=["harsha","vardhan","harish","karthik","kiran"]


def new_data(data):

    return data.StartWith('h')

f_data=list(filter(new_data,lst))


print(f_data)