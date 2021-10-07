a=[50,40,23,70,56,12,5,10,7]
i=1
sum=0
for i in a:
    sum+=1
print("sum",sum) 

a=[50,40,23,70,56,12,5,10,7]
maxno=a[9-2] 
for i in range(len(a)):
    if a[i]>maxno:
        maxno=a[i]
print("maxno in a:",maxno) 

a=[]
num=int(input("enter the element:"))
for i in range(1,num+1):
    b=int(input("enter element:"))
    a.append(b)
a.sort()
print("second largest element is:",a[num-2])

list=[2,2,3,4,5,6,7]
i=0
count=0
while i<len(list):#i=i+1 # count+=1
    i=i+1    
    print(i) 

#countnumeven num
list=[10,21,4,45,66,93]
num=0
count=0
while(num<len(list)):
    if num%2==0:
        print(list[num])
        count=count+1
    num+=1
print(count) 

#even num
list=[10,21,4,45,66,93]
num=0
count=0
while(num<len(list)):
    if num%2==0:
        print(list[num])
    num+=1

#oddnum
list=[10,21,4,45,66,93]
num=0
while(num<len(list)):
    if num%2!=0:
        print(list[num])
    num+=1

#max num in list
list=[1,2,3,4,5,6,7,8,9]
max=0
for i in list:
    if max<i:
        max=i
print(i) 


list=[38,5,10,35,39,86,85,86,85,20] 
i=0
l=[]
while i<len(list):
    if list[i]%5==0:
        l.append(list[i])
    i+=1   
print(l) 

number=["ram","gar"]
for i in reversed(number):
    print(i)

list=[10,20,30]
sum=sum(list)
len=len(list)
avg=sum/len      
print("avrage of given num in list is:",avg)  

n=int(input("how many element:"))
list=[]
for i in range(n):
    list.append(int(input()))
sum=sum(list)
len=len(list)
avg=sum/len
print("avrage of given num in list is:",avg) 



li=[1,2,3,4,5,6,6,7,8,9,10]
total=0
for number in li:
    if (number%2==0):
        total+=number    
print(total)

#sum of given list:"
num=[1,23,4,5,5,6,7]
i=0
sum=num[i]
while i<len(num):
    sum+=num[i]
    i=i+1
print(sum)  

     