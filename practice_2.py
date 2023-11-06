#multiplication if numbers
'''A=[]
n=int(input("enter the total number of rows"))
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    A.append(row)
print("matrix A is")
for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")
        print()
'''

#file handling
'''
f=open("myfile.txt","w")
f.write("hello python")
f.close()

f=open("myfile.txt","r")
f.read(10)
f.close()
'''

#seperate even and odd numbers form list
'''
li=[1,2,3,4,5,6,7,8,9,10]
even_list=[]
odd_list=[]
for i in li:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
'''

'''
f=open("myfile.txt","r")
print(f.read(20))
ch=f.read(20)
for i in ch:
    if i.isupper():
        print(i)
    elif i.islower():
        print(i)
'''   

















