#bubble sort
from array import *
num=int(input("Enter the total number of elements you want to insert"))
arr=array("i",[])
for i in  range(0,num):
    x=int(input("enter the array elements:"))
    arr.append(x)

print("Before sorting:",arr)

#applying logic to sort
for i in range(0,num):
    for j in range(0,num-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print("after sorting",arr)
    
