# i=1
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1
# print("sum:",sum)

# #sum=int(input("enter the 10 number"))
# i=1
# sum=0
# while i<=10:
#     num=int(input("enter the number"))
#     i=i+1
#     sum=sum+num
# print("sum is",sum)
    
# i=20
# while i>=1:
#     print(i)
#     i-=1



# i=0
# while i<=100:
#     if i!=0:
#         print(i)
#     i=i+7 


# i=0
# while i<=50:
#     if i!=0:
#         print(i)
#     i=i+5


# i=891
# while i<931:
#     z=i-890
#     if z%3==0:
#         print(z)
#     i=i+1


# i=891
# while i<931:
#     z=i-890
#     if z%3==0:
#         print(z)
#     i=i+1


# i=891
# while i<991:
#     z=i-890
#     if z%7==0:
#         print(z)
#     i=i+1


# i=-0
# while i<=99:
#     i=i+1
#     print(i)

# i=2
# while i<=99:
#     i=i+2
#     print(i)

# i=0
# while i<=99:
#     i=i+3
#     print(i)

# i=49
# while i<=98:
#     i=i+2
#     print(i)

# i=50
# while i<=100:
#     if i%2!=0:
#         print(i)
#     i=i+1
#    # print(i)

# i=50
# while i<=100:
#     if i%2!=0:
#         print(i)
#     i=i+1

# i=400
# while i>=350:
#     z=i-300
#     if z%2!=0:
#         print(z)
#     i=i-1    

# a=-1
# while a>=(-10):
#     print(-a)
#     a=a-1

# a=1
# while a<=10:
#     print(a)
#     a=a-(-10)


# a=1
# while a<=10:
#     print(a)
#     a=a-(-10)

# i=556
# while i<656:
#     z=i-555
#     if z%7==0:
#         print(z)
#     i=i+1

# #"divide by 7"    

# i=156
# while i<256:
#     j=i-155
#     if j%7==0:
#         print(j)
#     i=i+1

# #1 to 10 print:

# i=156
# j=i-155
# while j<=10:
#      print(j)
#      j=j+1


# #prime number     

# w=int(input("enter the enput"))
# count=0
# i=100
# while i<=w:
#     if w%1==0:
#         count=count+100
#     i=i+100
# if count==2:
#     print("prime")
# else:
#     print("not prime")

# #table    

# i=1
# while i<=10:
#     print(i*2)
#     i=i+1

# #"sum of 10 user input counter start with 50"    

# i=50
# j=51-50
# sum=0
# while j<=10:
#     num=int(input("enter the enput"))
#     j=j+1 
#     sum=sum+num
# print("sum is",sum)


# #divisible by 2 start with 20

# i=20
# while i<=100:
#     if i%2==0:
#         print(i)
#     i=i+1 


# #sum of 12 to 421
# i=12
# sum=0
# while i<=421:
#     sum=sum+i
#     i=i+1
# print("sum:",sum) 


# #multiple by 8 and sum:

# i=30
# sum=0
# while i<=420:
#     if i%8==0:
#         sum=sum+i
#     i=i+1
# print("sum:",sum)

# i=30
# sum=0
# while i<=420:
#     if i%8==0:
#         print(i)
#         sum=sum+i
#     i=i+1
# print("sum:",sum) 


# "#avrage"

# i=1
# sum=0
# avg=0
# while i<=11:
#     n=int(input("enter the num"))
#     sum=sum+n
#     i=i+1
#     print(sum)
#     avg=sum%11
#     if avg%5==0:
#         print(avg,"it is multiply by 5")
#     else:
#         print(avg,"it is not multiply by 5")

# #multiplication without using opreter:        

# num1=int(input("enter the first num:"))
# num2=int(input("enter the second num:"))
# sum=0
# for i in range(1,num1+1):
#     sum=sum+num2
# print("the multiplication of",num1,"and",num2,"is",sum) 

# #:fibonanacci series":

# n=int(input("enter the num"))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y


# #prime number:

# n=int(input("enter the enput:"))
# count=0
# i=1
# while(i<=n):
#     if(n%i==0):
#         count=count+1
#     i=i+1
# if(count==2):
#     print("prime number")
# else:
#     print("composite number")

# #print star:     

# n=int(input("enter the number"))
# for i in range(n):
#     print("","*"*(n*2))
#     n=n+1


# #sum of digit:

# n=int(input("enter the number to find of sum of digit"))
# sum=0
# while(n>0):
#     sum=sum+n%10
#     n=n//10
# print("sum of digit=",sum)

# #enter to digit:

# n=int(input("enter the number to find of sum of digit"))
# a=int(input("enter the enput"))
# sum=0
# while(n>0):
#     sum=a+n%10
#     n=n//10
# print("sum of digit=",sum) 

# #print star piramid shap:

# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end="")
#         b=b+1
#     j=1 
#     while j<=k:
#         print("*",end="")
#         j=j+1
#     k=k+2
#     print()
#     i=i+1 

# #print star reverse piramid shape:

# n=int(input("enter the row number"))
# i=1
# while(n>0):
#     b=1
#     while(b<i):
#         print(" ",end="")
#         b=b+1
#     j=1
#     while(j<=(n*2)-1):
#         print("*",end="")
#         j=j+1
#     print()
#     n=n-1
#     i=i+1

# #code out:    

# c=0
# d=1
# while c<3:
#     c=c+1
#     d=d*c
#     print("loop ke andar",c,d)
# else:
#     print("loop ke bahar",c,d)


# n=6
# s=0
# i=1
# while i<=n:
#     s=s+i
#     i=i+1
# print(s)

# #debug
# index=1
# while index<=10:
#     print(index)
#     index=index+1



# i=1
# k=65
# while i<=5:
#     j=1
#     while j<=i:
#         print(chr(k),end="")
#         j=j+1
#     k=k+1
#     print()
#     i=i+1


# i=1
# k=65
# while i<=7:
#     j=1
#     while j<=i:
#         print(chr(k),end="")
#         k=k+1
#         j=j+1      
#     print()
#     i=i+1

# rows=5
# b=0
# for i in range(rows,0,-1):
#     b+=1
#     for j in range(1,i+1):
#         print(b,end="")
#     print('\r') 

# row=14
# print("*"*row,end="\n")
# i=(row//2)-1
# j=2
# while i!=0:
#     while j<=(row-2):
#         print("*"*i,end="")
#         print(" "*j,end="")
#         print("*"*i,end="\n")
#         i=i-1
#         j=j+2 

# n=int(input("enter the number"))
# i=1
# while i<=100:
#     if i%3==0:
#         print("nav")
#     elif i%7==0:
#         print("gurukul")
#     elif i%3==0 and i%7==0:
#         print("navgurukul")
#     else:
#         print(i)
#     i=i+1 

# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print (i,"*",j,'=',i*j)
#         j+=1
#     i+=1
#     print("\n")


# #prime number:

# i=2
# while(i<100):
#     j=2
#     while(j<=(i/j)):
#         if not(i%j):
#             break
#         j=j+1
#     if(j>i/j):
#         print(i)
#     i=i+1 
# print("good bye") 


# #continue:
# i=0
# while i<10:
#     i=i+1
#     if i==3:
#         continue
#     print(i)

# #triangular number:count_1=   

sum=0
i=1
while i<=10:
    sum=sum+i
    print(sum)
    i=i+1  

# count_1=10
# count_2=100
# while count_1<=20 and count_2>=0:
#     print(count_1,count_2)
#     count_1=count_1+2
#     count_2=count_2+10
# print("end yhe loop")


# num=int(input("enter the number"))
# fact=1
# if num<=0:
#     print("fact does not def for neg int")
# elif(num==0):
#     print("the fact off 0 is 1")
# else:
#     while num>0:
#         fact=fact*num
#         num=num-1
#     print("fact of given number is")
#     print(fact) 

# i=6
# while i>0:
#     j=6
#     while j>i:
#         print("*",end=' ')
#         j-=1
#     i-=1
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=' ')
#     print()

# i=1
# j=11
# while i<=10:
#     while j<=20:
#         print(i,"*",j)
#         j=j+1
#         i=i+1 


# i=1
# j=11
# while i<=10:
#     while j<=20:
#             print(i,"*",j)
#             j=j+1
#             i=i+1

# num=1
# while num<=100:
#     print(num)
#     num=num+3

# num=100
# while num>=1:
#     print(num,"*")
#     num=num-1
# else:
#     print("loop is finised")    

