about="""If you want, I can give:
👉 Real-time example where not closing file causes bug
👉 OR MCQs for interview practice"""


fp=open('da.text','w')
newfile=fp.write(about)

print(newfile)

fp.close()