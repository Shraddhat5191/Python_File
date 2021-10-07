user=int(input("enter the num"))
rev=0
x=user
while(user>0):
    rev=(rev*10)+user%10
    user=user//10
if(x==rev):
    print("palindrme num")
else:
    print("not palindrome num")        