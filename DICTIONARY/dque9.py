s="MISSISSIPPI"
i=0
a=b=c=d=0
e={}
while i <len(s):
    if s[i]=="M":
        a=a+1
    if s[i]=="I":
        b=b+1
    if s[i]=="S":
        c=c+1
    if s[i]=="P":
        d=d+1
    i=i+1
l=("M:",a,"I:",b,"S:",c,"p:",d)
print(l)
# 
# d=dict()
# for c in s:
#     if c not in d:
#         d[c]=1
#     else:
#         d[c]=d[c]+1
# printdict = {'T1': ['eggs', 'bacon', 'sausage'], 'T2': ['bread', 'butter', 'tosti']}


# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# t = 0
# for value in dict:
#     value = dict[value]
#     count = len(value)
#     t += count
# print(t)

