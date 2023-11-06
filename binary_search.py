#binary search

num=int(input("Enter the number to search:"))
def search(l1):
    found=0
    l=0
    h=4
    while(l<=h):
        mid=(l+h)//2
        if l1[mid]==num:
            found=1
            print("value found")
            break;
        elif(l1[mid]>num):
            h=mid-1
        else:
            l=mid+1
    if(l>=h and found==0):
        print("value not found")


l1=[1,2,3,4,5]
search(l1)


            
        

  

    


