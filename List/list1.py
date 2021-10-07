#a=[10,11,12,13,14,15,16,17]
#print("a before reverse:",a)
#a2=a[::-1]
#print("a after revers:",a2)

#myl=[10,12,13,14,15,16,17,18]
#print("myl before reverse:",myl)
#myl.reverse()
#print("myl after reverse:",myl)

l=[10,20,30,5,45,99]
mx=max(l[0],l[1])
smax=min(l[0],l[1])
n=(l)
for i in l(n):
    if l[i]<mx:
        smax=mx
    elif l[i]<smax:
        mx!=l[i]
print("smax highest number is:",smax)

#find num >20 and <40:
list=[50,20,30,23,40,50,45,10,7]
i=0
count=0
a=[]
while i<len(list):
    if list[i]>20 and list[i]<40:
        a.append(list[i])
        count=count+1
    i=i+1
print(a)    
print(count) 