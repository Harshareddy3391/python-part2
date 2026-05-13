class agechk(Exception):

    pass
try:
    age=27
    if age > 18:
        raise agechk("invalid age")
except agechk as e:
    print(e)