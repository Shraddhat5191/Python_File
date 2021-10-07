# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
# b=" "
# a=name[0]+b+"the"+b+animal[0]+b+"is"+b+str(age[0])
# e=name[1]+b+"the"+b+animal[1]+b+"is"+b+str(age[1])
# c=name[2]+b+"the"+b+animal[2]+b+"is"+b+str(age[2])
# d=name[3]+b+"the"+b+animal[3]+b+"is"+b+str(age[3])    
# print(a)
# print(e)
# print(c)
# print(d)
    # print(b)
    # print(c)
    # print(d)

#Expected output
#=> Snowball the Cat is 1
#=> Chewy the Dog is 2
#=> Bubbles the Fish is 2
#=> Gruff the Goat is 6    


#Expected output
#=> Snowball the Cat is 1
#=> Chewy the Dog is 2
# #=> Bubbles the Fish is 2
# #=> Gruff the Goat is 6
# a=[1,2,3,4]
# b=[1,2,3,4]
# i=0
# while i<len(a):
#     t=(a[i])
#     i=i+1
#     print(t)
    # s=0
    # while s<len(b):
    #     k=(b[-s])
    #     i=i+1
    #     print(k)    
#s=0
# while i<len(a):
#     d=a[i],b[-i]
#     i=i+1
#print(d)

# # a=[1,2,3,4]
# list=[1,2[3,4[6]]
# print(list)[0]=[1]
# print(list)[1]=2
# print(list)[2]=[3,4]
# print(list)[1][0]=3
# print(list)[1][1]=4
# print(list)[2]=[6]
# print(list)[2][0]=6

#Python Nested List Indexing

# L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']


#print(L[2][0])
# Prints ['cc', 'dd', ['eee', 'fff']]

#print(L[2][2][0])=a
#repleace.(L[2][2][])
# Prints ['eee', 'fff']

#print(L[2][2][0])
#a=[3,5,6,7]                                                                                                                                                                                               
#a[0]=2
#print(a)
# ge the value of a specific item in a nested list by referring to its index nrint(L)
# Print['a', ['bb', 0], 'd']

# a=[[[[[1,2,3]]]]]
# a[0][0][0][0][0]=4
# #a[0][0][0][0][1]=5
# # a[0][0][0][0][2]=7
# print(a)


# a=[[[[[3,5,6,7]]]]]
# a[0][0][0][0]=4
# a[0][0][0][1]=6
# a[0][0][0][0][2]=8
#  print(a)
# # 

# L = ['a', ['bb', 'cc'], 'd']
# # L[1].insert(0,'xx')
# L[1].insert(1,'aa')
# print(L)
# # Prints ['a', ['xx', 'bb', 'cc'], 'd']


# a=[[[[[[[3,5,6,7]]]]]]]
# a[0][0][0][0][0][0][0]=1
# a[0][0][0][0][0][0][1]=2
# a[0][0][0][0][0][0][2]=3
# a[0][0][0][0][0][0][3]=4
# # a[0][0][0][0][0]=2
# print(a)




# # L = ['a', ['bb', 'cc'], 'd']
# # L[1].extend([1,2,3])
# # print(L)
# # Prints ['a', ['bb', 'cc', 1, 2, 3], 'd']

 



# # pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
# # # pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3] 

# # for p in pat:
# #     pass
# #     if (p == 0):
# #         current = p
# #         break
# #     elif (p % 2 == 0):
# #         continue
# #     print(p)    

# # print(current)
# # pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
# # pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3] 
# # pat = [1


# a=[[[[[[[3,5,6,7]]]]]]]
# a[0][0][0][0][0]=1
# a[0][0][0][0][0][0][0]=2
# a[0][0][0][0][0][0][1]=2
# a[0][0][0][0][0][0][2]=3
# a[0][0][0][0][0][0][3]=4
# print(a)

 
a=[2,3,4,[1,5],43,[78,54],56]

print(a[0][2][0])