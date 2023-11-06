'''n=int(input("enter the number"))
x=1
root=0.5*(x+(n/x))
print("square root of",n,"is :",root)
'''

#through funtion
def squareroot(n,x):
    root=0.5*(x+(n/x))
    return root
n=int(input("enter the number"))
x=int(input("enter the random number"))
print(squareroot(n,x))

