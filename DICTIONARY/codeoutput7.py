# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

rec = {
    "Name" : "Python", 
    "Age":"20", 
    "Addr" : "NJ", 
    "Country" : "USA"
    }
id2 = id(rec)
print(id == id2)

 
# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }

# print(details["name"])
# print(details["email"])
# print(details["age"])


# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+i
# print(sum)
 
# c=dict()
# for i in range(1,16):
#     c[i]=i**2
# print(c)
# dict={'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita'}

# dict={{"first":"1"}, {"second": "2"}, {"third": "1"},{"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}}
 
# list =[] # create empty list
# for val in dict.values(): 
#   if val in list: 
#     continue 
#   else:
#     list.append(val)

# print (list)


 
s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
c={}
for i in (s,a):
    c.update(i)
print(c)

 