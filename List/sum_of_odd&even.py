list=[10,21,4,45,66,93]
j=0
sum=0
while(j<len(list)):
    # j=j+1
    if list[j]%2==0:
        sum=sum+list[j]
    else:
        sum=sum+list[j]
    j=j+1    
        
print("\n the sum of even in this list=", sum)
print("the sum of odd numberin this list=", sum)            
