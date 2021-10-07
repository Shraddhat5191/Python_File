from collections import Counter
# my_dict = {'T': 23, 'U': 22, 'T': 21,'O': 20, 'R': 32, 'S': 99}
my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
k = Counter(my_dict)
# 3 highest values
high= k.most_common(4)
s=[]
#three hightest values
# ("Keys=0 : Values=1")
for i in high:
    s.append(i[1])
#    print(i[0]," : ",i[1]," ")
print(i[1])
# print(my_dict[i])
print(s)    
