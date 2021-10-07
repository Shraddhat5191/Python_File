# bank_list=open("file-question3.txt","w")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
banks_list1=open("fil_question3.txt","w")
i=0
while i<len(banks_list):
    banks_list1.write(banks_list[i])
    banks_list1.write("\n")
    i=i+1
banks_list1.close()    

# a="\n"
# for i in (a):
#     print(a)
# bank_list.close()

