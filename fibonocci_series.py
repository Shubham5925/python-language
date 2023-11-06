num=int(input("Enter the number"))
if num>0:
    if num==0:
        print ("0")

    elif num==1:
        print("1")

    else:
        c=0
        while c<num:
            a=0
            b=1
            print(c,end="")
            c=a+b
            a,b=b,c
            c=c+1
            
            
            
