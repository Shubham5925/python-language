num=int(input("Enter the number"))
temp=num
f=0
while(temp>0):
    rem=temp%10
    s=rem**3
    f=f+s
    temp=temp//10

if(f==num):
    print("Armstrong number")
else:
    print("Not armstrong number")
