a=[2,2,2,2,2]
b=[2,2,2,2,2]
i=0
sum=0
c=[]
while i<len(a):
    sum=sum+a[i]+b[i]
    c.append(a[i]+b[i])
    i=i+1
print(c)                         