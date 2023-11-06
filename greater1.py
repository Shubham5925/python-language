x=int(input("enter the 1st number"))
y=int(input("enter the 2nd number"))
z=int(input("enter the 3nd number"))
if(x>y and x>z):
 print(x," is greater.")
else:
    if(y>x and y>z):
        print(y," is greater.")
    else:
        print(z,"is greater")
