about="""If you want, I can give:
Real-time example where not closing file causes bug
OR MCQs for interview practice   y Responsibilities: • Attend and resolve machine breakdowns promptly to minimize downtime • Execute preventive maintenance activities as per schedule • Basic understanding and troubleshooting of control systems and mechanical components • Manage and track spare parts inventory to ensure availability • Support maintenance and monitoring of utility systems such as DG sets, compressors, and fire hydrant systems • Ensure proper functioning of plant lighting systems • Maintain records of maintenance activities and report issues proactively • Follow safety standards and ensure compliance during all maintenance activities Requirements: • 23 years of relevant maintenance experience in manufacturing/plant environment • Diploma / ITI in Electrical & Electronics • Hands-on experience in electrical maintenance and basic mechanical systems • Knowledge of u"""

"""
fp=open('da.text','w')
newfile=fp.write(about)

 

print(newfile)

fp.close()

"""
"""
with open('da.text','r') as f:
    filedataread=f.read()

    print(filedataread)

    f.close"""

fp=open('d.txt','w+')
 
adddata=fp.write("\nhello good morging")
data=fp.read()
print(data)

fp.close()