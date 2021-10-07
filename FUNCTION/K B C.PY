# def kbc(s,t):
#     a=s+t
#     return a
# a=int(input("enter the no"))
# b=int(input("enter the no"))    
# d=kbc(a,b)
# print(d) 





question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1] 
ans_list=[
    ["1 Nine","2 Seven"],
    ["1 Bhopal","2 Delhi"],
    ["1 Software Engineering","2 Counseling"]
    ]
answere_list=[2,2,1]
i=0
count=0
amount=0
a=1
b=0
while i<len(question_list):
    print(question_list[i])
    i=i+1
    j=0
    b=i
    while j<len(options_list):
        k=options_list[j][b]
        # print(j+i,k)
        print(options_list[i])
        j=j+1
    user=input("Do You Want Life Line ")
    if user=="yes":
        print(5050)
        if count==0:
            print(answere_list[b])
            user2=int(input("enter the your answer:"))
            if user2==ans_list[i]:
                amount+=10000
                print("your answer is corect:")
                print("you won",amount)
            else:
                print("your answer is wrong:")
                print("you loose the game")
                break
            count=count+1
        else:
            print("sorry you can'tlifeline agine")
            user3=int(input("select your answer"))
            if user3==solution_list[i]:
                print("congrate right answer")
                amount+=10000
                print("you won",amount)
            else:
                print("your answer is wrong")
                print("you loose the game")
                break
    elif user=="no":
        user4=int(input("select answer"))
        if user4==solution_list[i]:
            amount=10000
            print("coggrats right answere")
            print("you won2",amount)
        else:
            print("your answere is wrong")
            print("you loose the game")
            break
    else:    
        print("nothing")
    amount=amount+10000
    i=i+1
    a=a+1
    b=b+1                           


