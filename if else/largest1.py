num1=int(input("enter the enput"))
num2=int(input("enter the enput"))
num3=int(input("enter the enput"))
if num2>num1 or num2>num3:
    print("largest num1")
    if num1>num2 or num1>num3:
        print("largest num2") 
        if num2>num3 or num3>num2:
            print("less num3")
        else:
            print("num3 not largest")
    else:
        print("num2 not lergest")
else:
    print("num1 not largest")                                           

