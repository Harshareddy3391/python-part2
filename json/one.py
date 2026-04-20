import json
"""

jsondata='''{"name":"harsha","status":true}'''

data=json.loads(jsondata)


print(jsondata)
print(type(jsondata))
print(type(data))
print(data)"""



dir={'name': 'harsha', 'status': True}


da=json.load(dir)

print(type(dir))
print(type(da))