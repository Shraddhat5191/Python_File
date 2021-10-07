i=10
a=[]
while i>0:
    print("enter the number")
    num=input()
    a.append(num)
    i=i-1
#print(a)    
print("enter the number")
n=input()
i=9
count=0
while i>=0:
    if n==a[i]:
        print("yes")
        count=count+1
    i=i-1
if count==0:
    print("no")

