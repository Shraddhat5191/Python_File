n=int(input("enter the harsad number:+"))
# k=n.split()
sum=0
i=n
n_123=list(str(n))
while i > 0:
    s=1%10
    sum=sum+s
    i=i//10
if n%sum==0:
    print(n_123,"harsad")
else:
    print(n_123,"not harsad")

 
# x = 42
# x_digits = list(str(x)


# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
# i=0
# y=[]
# while i<len(marks):
#     s=0
#     t=marks[i][0]
#     while s<len(marks[i]):
#         if marks[i][s]>t:
#             t=marks[i][s]
#         s=s+1
#     i=i+1
#     y.append(t)
# print(y)    





