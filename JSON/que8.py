a=["name","degination","age","salary"]
b=["neelam","programar","24","2400"]
ab={}
ab1={}
ab2={}
ab3={}
f={}
y=0
for x in a:
    ab[x]=b[y]
    y=y+1
# print(ab)
f["employee"]=ab
a=["name","degination","age",'salary']
b=["komal","trainer","24","20000"]
# ab={}
y=0
for x in a:
    ab1[x]=b[y]
    y=y+1
# print(ab1)
f["employee1"]=ab1
a=["name","degination","age","salary"]
b=["anuradha","HR","25","40000"]
# ab={}
y=0
for x in a:
    ab2[x]=b[y]
    y=y+1
# print(ab2)
f["employee3"]=ab2
a=["name","degination","age","salary"]
b=["abhishek","manager","29","63000"]
# ab={}
y=0
for x in a:
    ab3[x]=b[y]
    y=y+1
# print(ab3) 
f["employee4"]=ab3  
import json 
with open("piyuu.json","w") as a:
    json.dump(f,a,indent=3)

