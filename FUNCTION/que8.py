# Ek function likho jo ki ek argument le 
# jo number ho or dictionary return karega jisme
#  keys 1 se lekar argument ke number tak hogi aur values unke 
# squares honge.jaisa ki niche dikhaya gaya hai:-input output = 20 

def dict(num):
    k=1
    d={}
    while k<=num:
        value=k**2
        d[k]=value
        k=k+1
    return(d)
a=int(input("enter the input:")) 
print(dict(a))       


