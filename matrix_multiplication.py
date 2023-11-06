'''a=[[1,2,3],[1,2,3],[1,2,3]]
b=[[1,2,3],[1,2,3],[1,2,3]]
c=[[1,2,3],[1,2,3],[1,2,3]]
result=[[],[]]
print(a)
print(b)
print(c)
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            result[i][j]=a[i][k]*b[k][j]
print(result)
'''

A=[]
for i in range(3):
    row=[]
    for i in range(3):
        row.append(int(input("enter the row elements of A")))
    A.append(row)
print(A)


B=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(int(input("enter the row elements of B")))
    B.append(row)
print(B)


result=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(0)
    result.append(row) 
print(result)

for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(result)):
            result[i][j]=A[i][k]+B[k][j]
print(result)











    
