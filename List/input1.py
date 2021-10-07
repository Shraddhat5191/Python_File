  
list=[1,2,3,4,5,6,7,8,9]
user=int(input("enter a number"))
i=-1
list1=[]
while i<len(list):
    list1.append(list[i])
    # print(a[i])
    if list[i]==user:
        break
    i=i-1
print(list1)