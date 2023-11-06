x=int(input("enter your percentage"))
if(x<=40):
    print("POOR")
elif(x>40 or x<70):
    print("GOOD")
elif(x<70 or x>85):
    print(" VERY GOOD")
else:
    print("EXCELLENT")
