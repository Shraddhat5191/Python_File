list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
a=[]
i=0
while i<len(list1):
    b=list1[i]
    if b is not list2:
        a.append(b)
    i=i+1
print(a) 


# [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# a=[]
# i=0
# while i<len(list1):
#     b=list1[i]
#     if b in list2:
#         a.append(b)
#     i=i+1
# print(a


# def numbers_less_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:
#       list.remove(item)
#     else:
#       counter += 1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

# num_list_sub_20 = numbers_less_than_twenty(num_list)

# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20) 