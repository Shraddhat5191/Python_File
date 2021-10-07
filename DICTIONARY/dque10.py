dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
t = 0
for value in dict:
    value = dict[value]
    count = len(value)
    t += count
print(t)    
