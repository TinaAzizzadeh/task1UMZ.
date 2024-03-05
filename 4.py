a=input("type(1)for c to f and type(2)for f to c:")
if(a=="1"):
    c=int(input("enter your number:"))
    f=(c*1.8)+32
    print("result=",f)
elif(a=="2"):
    f=int(input("enter your number:"))
    c=(f-32)/1.8
    print("result=",c)
else:
    print("invalid number")