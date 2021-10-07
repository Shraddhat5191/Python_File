card=input("enter the card name")
if card=="dabidcard" or "creaditcard":    
    print("transaction process")
    language=input("enter the language")
    if language=="english" or language=="hindi":
        print("select your language")
        pincode=int(input("enter pincode"))
        if pincode==1234:
            print("pincode accept")
            account=input("type of account")
            if account=="saving account" or "curent account":
                print("account accept")
                amount=int(input("enter amount"))
                if amount<=10000:
                    print("amount preped")
                    recipt=input("i want recipt")
                    if recipt=="yes":
                        print("accept")
                    else:
                        print("not accept")
                else:
                    print("amount not preped")
            else:
                print("account not accept")
        else:
            print("pincode not accept")
    else:
        print("not my language") 
else:
    print("card is not accept")