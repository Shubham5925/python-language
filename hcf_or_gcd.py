n1=int(input("enter the number 1"))
n2=int(input("enter the second number 2"))
if n1>n2:
    for i in range(1,n1):
        if n1%i==0 and n2%i==0:
            hcf=i
        else:
            continue
if n2>n1:
    for i in range(1,n2):
        if n1%i==0 and n2%i==0:
            hcf=i
        else:
            continue
print(hcf)
