# def calculator (num1,num2):
#     k=num1*num2
#     print(k)
# a=int(input("enter the number"))    
# b=int(input("enter the number")) 
# calculator(a,b) 
# 
def calculator (num1,num2):
    i=0
    a=[]
    while i<len(num1):
        s=0
        while s<len(num2):
            k=num1[i]*num2[i]
            a.append(k)
            s=s+1
            i=i+1
        print(a)
        a.append(k)
        s=s+1
        i=i+1
calculator ([5, 10, 50, 20],[2, 20,3,5])  
