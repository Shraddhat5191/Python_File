username=input("enter the fecbook account").lower()
if username=="ram":
    print("wemcome in fecbook account")
    num=int(input("enter the num"))
    if num==1234:
        passward=input("enter the passward")
        if passward=="shr123":
            print("successful")
        else:
            print("passward wrong")
    else:
        print("num wrong")
else:
    print("user name wrong create new fecbook account")
    newname=input("enter the first name")
    lastname=input("enter the last name")
    dob=int(input("enter the birth date"))
    phone=input("enter your mobile number or email i'd ")
    newpass=input("enter your password")
    print("your ac has been created")