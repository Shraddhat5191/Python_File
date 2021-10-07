marks=[[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
i=0
y=[]
while i<len(marks):
    s=0
    t=marks[i][0]
    while s<len(marks[i]):
        if marks[i][s]>t:
            t=marks[i][s]
        s=s+1
    i=i+1
    y.append(t)
print(y) 