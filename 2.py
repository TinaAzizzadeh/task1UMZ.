a=int(input("enter your m:"))
o=True
while(o==True):
    g=input("type(w)for withdraw,type(d)for deposit,type(m)to check your balance:")
    if(g=="w"):
        b=int(input("enter your number:"))
        a=a-b
    elif(g=="d"):
        b=int(input("enter a number:"))
        a=a+b
    elif(g=="m"):
       print("result: ",a)
    if(g=="w"or g=="d"):
     t=input("do you want to check your balance(y/n)?")
     if(t=="y"):
      print("result: ",a)
    j=input("do you want to continue(y/n)?")
    if(j=="n"):
     o=False
    else:
     o=True