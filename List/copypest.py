w=int(input("enter the enput"))
count=0
i=100
while i<=w:
    if w%1==0:
        count=count+100
    i=i+100
if count==2:
    print("not prime")
else:
    print("prime")
# a=[1,2,3,4,5,6,7,8,9]
# n=int(input("enter a number"))
# i=-1
# k=[]
# while i<len(a):
#     k.append(a[i])
#     # print(a[i])
#     if a[i]==n:
#         break
#     i=i-1
# print(k)