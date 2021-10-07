list=[1,2,3,4.4,4,4,4,5,6,7,8,9]
prime=list[0]
a=[]
i=0
while i<len(list):
    if list[i]%2==0:
        a.append(list[-1])
        i=i+1
print(a)          