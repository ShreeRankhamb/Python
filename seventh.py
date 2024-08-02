#file input/output in python
#1.open
f=open("demo.txt","a")

f.write("\nHEllo welcome to Apna college")
#data=f.read()
#print(data)
#print(type(data))
f.close()

import os

os.remove("demo.txt")

#with syntax
with open("dem.txt","r") as f:
    data=f.read()
    print(data)



