# class dictObj(object):
#      def __init__(self):
#          self.x = 'red'
#          self.y = 'Yellow'
#          self.z = 'Green'
#      def do_nothing(self):
#          pass
# test = dictObj()
# print(test.__dict__)


# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(d)

a={1:12,2:23}
it=a.items()
print(it)
# print()
lst=list(it)
print(lst)
# print(type(lst))
# print(lst[0][0])
print(lst[0][0])




# import itertools      
# d ={'1':['a','b'], '2':['c','d']}
# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
#     print(''.join(combo))



# Python Code:

# from collections import defaultdict, Counter
# str1 = 'w3resource' 
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

    


# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)
# # 
# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])

# print(person[4])

# result = person[4]['place']

# print(result)

# a={1:12,2:23,3:34,4:45}
# print(a[4])     
