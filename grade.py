e=int(input("enter the marks of english"))
p=int(input("enter the marks of physics"))
c=int(input("enter the marks of chemistry"))
m=int(input("enter the marks of maths"))
marks=(e+p+c+m)/4;
if(marks>=75):
    print("A")
elif(makrs>=60 and marks<=75):
    print("1st division")
elif(marks>=50 and marks<60):
    print("2nd division")
elif(marks>=40 and marks<50):
    print("3rd division")
else:
    print("fail")

