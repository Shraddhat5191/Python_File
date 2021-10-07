year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it is leep year")
        else:
            print("it is century year")
    else:
        print("it is leap year")
else:
    print("it is not leap year")
