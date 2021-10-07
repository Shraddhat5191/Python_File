student=[23,45,6,89,90,54,34,21,34,23,19,10,45,80,87]
list=len(student)       
i=0
lessthan50=0
morethen=0
while i<list:
    mark=student[i]
    if mark<50:
        lessthen50=lessthen50+1
    else:
        morethen=lessthen50+1
    i=i+1
print("mark morethen50:",+str(lessthan50))
print("mark lessthen50:",+str(morethen))            