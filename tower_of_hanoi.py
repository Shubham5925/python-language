#Tower of hanoi
def toh(n,a,b,c):
    if n==1:
        print("move disc",n,"from" ,a,"to",c)
    else:
        toh(n-1,a,c,b)
        print("move disc",n,"from",a,"to",c)
        toh(n-1,b,a,c)

toh(3,'A','B','C')
