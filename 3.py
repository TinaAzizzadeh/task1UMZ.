a=input("enter op:")
b=int(input("enter first number:"))
c=int(input("enter second number:"))
if(a=="divide"):
    d=b/c
elif(a=="multiple"):
    d=b*c
elif(a=="difference"):
    d=b-c
elif(a=="sum"):
    d=b+c
print(d)