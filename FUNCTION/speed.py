def driver_s(speed):
    i=75
    a=0
    while i<=speed:
        if speed>70:
            a=a+1
            i=i+5
        print("a",a)
    if speed<70:
        print("ok")        
    if speed>12:
        print("licencence suspended")
speed=int(input("enter the num"))
# b=int(input("enter the num"))
driver_s(speed)        

