# num=[50,20,30,23,40,50,45,10,7]
# even_sum=0
# count=0
# odd_sum=0
# count=0
# for j in range(len(num)):
#     if (num[j]%2==0):
#         even_sum=even_sum+num[j]
#         count=count+1
#     else:
#         odd_sum=odd_sum+num[j]
#         count=count+1
# list=[18,58,66,85,25,51]
# even_sum=0
# odd_sum=0
# j=0
# count=0
# while(j<len(list)):
#     if(list[j]%2==0):
#         even_sum=even_sum+list[j]
#         count=count+1
#     else:
#         odd_sum=odd_sum+list[j]
#         count=count+1
#     j=j+1
# print("the sum of given number in the list=",even_sum)
# print("the sum of given number in the list=",odd_sum)

list=[18,58,66,85,25,5,10]
count1=0
count2=0
even=[]
odd=[]
sum=0
sum1=0
i=0
while i<len(list):
    if list[i]%2==0:
        even.append(list[i])
        count1=count1+1 
        sum=sum+list[i]                                                         
    else:
        odd.append(list[i])
        count2=count2+1
        sum1=sum1+(list[i])
    i+=1    
print("the count of enen num in given list=",even,count1,sum)
print("the count of odd num in given list=",odd,count2,sum1)

list1=["m","na","i","ki"]
list2=["y","me","s","lly"]
i=0
a=[]
while i<len(list1[0]):
    l=list1[0]+list2[0],list1[1]+list2[1],list1[2]+list2[2],list1[3]+list2[3]
    a.append(l)
    i=i+1
    print(a)


                  

