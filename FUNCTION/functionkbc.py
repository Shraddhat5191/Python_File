def questions():
    question_1 = [
        "How many continents are there?",              
        "What is the capital of India?",            
        "NG mei kaun se course padhaya jaata hai?"    
    ]
    return question_1
questions_1=questions()

def options():
    options_1 = [
        #pehle question ke liye options
        ["Four", "Nine", "Seven", "Eight"],
        #second question ke liye options
        ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
        #third question ke liye options
        ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
    ]
    return options_1
options_1=options()

def solution():
    solution_1 = [3, 4,1]
    return solution_1

solution_1=solution()


def answers():
    answer_list=[
        ["1 four","3 seven"],
        ["2 Bhopal","4 Delhi"],
        ["1 software engineering","4 agriculture"]
     
    ]
    return answer_list
answers_1=answers()
print("kon banega crorepati ")
i=0
s=0
count=0
while i<len(questions_1):
    print(questions_1[i])
    a=0
    b=i
    while a<len(options_1[i]):
        k=options_1[b][a]
        print(a+1,k)
        a=a+1
    if count<1:
        num1=input("do you want 5050 lifeline : ")

        if num1=="yes":
            k=0
            while k<len(answers_1[i]):
                print(answers_1[b][k])
                k+=1
            # print(answers_new[b])
            num2=int(input("enter your answer"))
            if num2==solution_1[i]:
                s+=10000
                print(" right answer")
                print ("you win : ",s)
            else:
                print("worng answer")
                print("you can't play again")
                print("you win : ",s)
                break
            count+=1
            
        else:
            pass
            m=int(input("enter your answer:"))
            if m==solution_1[i]:
                print("right answer ")
                s+=10000
                print("you win : ",s)
            else:
                print("No chance")
                print("your answer is wrong :")
                print("you win : ",s)
                break
              
    else:
        pass
        k=int(input("enter your answer : "))
        if k==solution_1[i]:
            print("right answer")
            s+=10000
            print("you win : ",s)
        else:
            print("no chance")
            print("your answer is wrong")
            print("you win : ",s)
            break
    i=i+1
    print("congrulation")
    print("you win : ",s)
    print("thankyou")


