def countlo(santense):
    upper=0
    lower=0
    for i in santense:
        if i>="A" and i<="Z":
            upper=upper+1
        elif i>="a" and i<="z":
            lower=lower+1
    print("upper case:"+str(upper))
    print("lower cse:"+str(lower))
countlo("The quick Brow Fox")                