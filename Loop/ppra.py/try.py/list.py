#sum of given list:
#num=[2,2,2,2,2]
#i=0
#sum=0
#a=[]
#while i<len(num)
    #s=num[i]  #this is not importent
    #sum=sum+s #sum=sum+num[i]
 #   i=i+1
#print(sum)


# place in revarse:
place=["shraddha","tiwari","varsha","namita","komal"]
i=0
c=[]
while i<len(place):
    c.append(place[-i])
    i=i+1
print(c)

#num=30
#n=[10,11,12,13,14,17,18,19]
#i=0
#a=[]
#while i<len(n):
    #b=0
    #while b<len(n):
        #if n[i]+n[b]==num:
       #     c=([n[i],n[b]])
      #      a.append(c)
  #      b=b+1
 #   i=i+1        
#print(a) 

ram=["a","r","a","d","a","f","b","a","d","r"]
i=0
m=[]
while i<len(ram):
    b=0
    count=0
    n=[]
    while b<len(ram):
        if ram[i]==ram[b]:
            count=count+1
        b=b+1
    n.append(ram[i])
    n.append(count)
    if n not in m:
        m.append(n)
    i=i+1
print(m) 

