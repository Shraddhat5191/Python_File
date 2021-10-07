list=[1,2,3,2,13,12,12,32]
Index=0
while Index<len(list):
    j=Index+1
    while j<len(list):
        if list[Index]==list[j]:
            del(list[j])
        j=j+1
    Index=Index+1
print(list)      