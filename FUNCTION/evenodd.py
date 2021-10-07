def check_numbers(num1,num2):
    i=0
    while i<len(num1):
        s=0
        while s<len(num2):
            if num1[i]%2==0 and num2[s]%2==0:
                print("dono even hai")
            else:
                print("dono even naahi hai")
            s=s+1
            i=i+1
check_numbers([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])