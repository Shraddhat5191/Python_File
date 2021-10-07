physics= int(input("enter the input1"))
chemistry= int(input("enter the input2"))
biology= int(input("enter the input"))
mathematics= int(input("enter the input3"))
computer= int(input("enter the input"))
Total=physics+chemistry+biology+mathematics+computer
percentage=(Total/500.0)*100
if percentage<40:
    print("F")
elif percentage>=30 and percentage<=40:
    print("E")
elif percentage>=50 and percentage<=60:
    print("D")
elif percentage>=70 and percentage<=80:
    print("C")
elif percentage>=90 and percentage<=100:
    print("B") 
elif percentage>=100 and percentage<=1110:
    print("A")