list=[1,2,3,4,5,6,7,8,9,10]
print(list)
l=len(list)
for i in range(0,1):
    c=0
    for j in range(2,list[i]):
        if list[i]%j==0:
            c=1
            break
    if c==0:
        print(list[i],"is prime num")
    else:
        print(list[i],"is not prime num")        