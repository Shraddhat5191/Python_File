row=6
for i in range(1,row):
    num=1
    for j in range(row,0,-1):
        if j>i:
            print(" ",end="")
        else:
            print(num,end="")    
            num+=1
    print("")
i=row-1
for i in range(1,row):
    for j in range(i,0,-1):
        print(j,end="")
    print("")    





















 
                                