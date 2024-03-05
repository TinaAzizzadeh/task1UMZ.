a=input("enter :")
if(a.isdigit()==True):
 z=int(a)
 print(type(z))
elif(a.startswith("[")==True):
 z=list(a)
 print(type(z))
else:
   print(type(a))
