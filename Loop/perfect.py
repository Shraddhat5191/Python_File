per=int(input("percentage first"))
if per>80:
    print("we get good job")
    per=int(input("percentage sec"))
    if per>60 and per<80:
        print("we get job")        
        per=int(input("percentage thir"))
        if per>45 and per<=50:
            print("we are giving interview for job")
            per=int(input("percentage"))
            if per>25 and per<=45:
                print("we are doing pratice for intreview")
                per=int(input("percentage fort"))
                if per<25:
                    print("i not get job")
                else:
                    print("we  get job")
            else:
                print("we not doing practice")
        else:
            print("we not give interview")
    else:
        print("we not get job")
else:
    print("we not get")                                    

        


                

            






