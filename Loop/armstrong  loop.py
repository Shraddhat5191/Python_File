num=int(input("enter the chake for arm strong"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==num:
    print("number is armstrong")
else:
    print("number is not armstrong")    
