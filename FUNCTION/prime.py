# def prime(num1):
#     i=2
#     while i<num1:
#         if num1%i==0:
#             print(num1,"not prime no.")
#             break
#         i=i+1
#     else:
#         print(num1,"prime no.") 
# a=int(input("enter the number")
# # prime(a) 
# def prime(limit): 
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
# a=int(input("enter the enput"))     
# print("a")
# def prime(limit):
#     i=2
#     while(i<100):
#         j=2
#         while(j<=(i/j)):
#             if not(i%j):
#                 break
#             j=j+1
#         if(j>i/j):
#             print(i)
#         i=i+1
# a=int(input("enter the enput"))
# b=int(input("enter the enput"))
# print(a,b)
# def shraddha(a):
#     i=2                
#     while(i<100):
#         j=2
#         while(j<=(i/j)):
#             if not(i%j):
#                 break
#             j=j+1
#         if(j>i/j):
#             print(i)
#         i=i+1
# # shraddha(100)

# def count(sentense):
#     Upper=0
#     lower=0
#     for i in sentense:
#         if i>="A" and i<="Z":
#             Upper+=1
#         elif i>="a" and i<="z":
#             lower+=1
#     print("Upper case:"+str(Upper))
#     print("lower case:"+str(lower))
# count("The quick Brow Fox")
# 
# 

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for key in dic1:
    if key in dic2:
        dic2[key]=dic1[key]+dic2[key]
        dic2.update(dic3)
    else:
        dic2[key]=dic1[key]
print(dic2)

# s="python"
# rev=[]
# i=len(s)
# while i>0:
#     rev.append(i)
#     rev=rev+s[i]
#     i=i-1
# print("s",+str[i])    



           






