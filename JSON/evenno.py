  
# number=int(input("Please Enter a Number : "));  
# x=int(number/2)*2;  
# if(x==number):  
#     print("This Number is Even")    
# else:  
#     print("This Number is Odd")

list=[38,5,10,35,39,86,85,87,20]
i=0
l=[]
while i<len(list):
    if list[i]%2==0:
        l.append(list[i])
    i=i+1
print(l)