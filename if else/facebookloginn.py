username=input("enter the fecbbok account").lower()
if username=="ram":
    print("wemcome in fecbook account")
    mobile_number=int(input("enter the num"))
    if mobile_number==1234:
        passward=input("enter the passward")
        if passward=="shr123":
            print("successful")
        else:
            print("passward wrong")
    else:
        print("num wrong")
else:
    print("user name wrong create new fecbook account")
    first_name=input("enter the first name")
    if first_name>=("a to z"):
        lastname=input("enter the last name")
        if lastname>=("a to z"):
            your_email=input("enter the email")
            if your_email>="a to z" or "@r" or "o to 9":
                gander=input("enter the gander")
                if gander=="male" or "femail" or "other":
                    dob=input("enter the dob")
                    if dob==dob:
                        print("login sucessful")
                    else:
                         print("login not sucessful")
                else:
                     print("gander wrong")
            else:
                 print("email wrong")
        else:
            print("last name wrong")
    else:
        print("first name wrong")
                      
                                                            

                        
