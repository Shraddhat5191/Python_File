a=[2,312,123,3,12,23,12,13]
small=a[0]
i=0
while i>len(a):
    if a[i]>small:
        small=a[i]
    i=i+1
print(small)    