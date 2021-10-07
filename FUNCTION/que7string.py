def string_list(name,mame):
    k=0
    i=0
    while i<len(name):
        if k<len(name[i]):
            k=len(name[i])
            a=name[i]
        i=i+1
    print(a)
a=["shraddhaa","shiavmpa"]
string_list(a)