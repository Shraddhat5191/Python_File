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
# k=0    
k = Counter(my_dict)
# 3 highest values
high= k.most_common(3)
s=[]
# print("Dictionary with 3 highest values:")
# print("Keys : Values")
for i in high:
    s.append(i[1])
#    print(i[0]," : ",i[1]," ")
#    print(i[1])
print(s)


  


    