year=int(input("enter the enput"))
if year%4==0:
    print("it is leap year")
elif year%100==0:
    print("year is not leap year") 
elif year%400==0:
    print("it is not leap year")  
else:
    print("year is not leep year")