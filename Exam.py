print("Hloo word")

lst=[]
a=str(input("If you already have an account, enter /y/, otherwise enter /n/ :"))
if a=="y":
    x=str(input("Pleas Enter Frist Name :"))
    y=str(input("Pleas Enter Last Name :"))
    z=int(input("Pleas Enter Eja :"))
    xx=str(input("Pleas Enter Email :"))
    yy=str(input("Pleas Enter Passworde :"))
    lst.append(x)
    lst.append(y)
    lst.append(z)
    lst.append(xx)
    lst.append(yy)
if a=="n" :
    x=str(input("Pleas Enter Email :"))
    y=str(input("Pleas Enter Passworde :"))
print("Hi Master",x,"",y)
print(lst)