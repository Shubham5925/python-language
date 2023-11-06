#print("Hello world to python")

#multiple statement

'''
print("Hello")
print("World")
'''

#check even or odd
'''
num=int(input("Enter the number"))
if(num%2==0):
    print("Even")
else:
    print("Odd")
'''

#armstrong number
'''
n=int(input("Enter the number"))
flag=0
num=n
while(num>0):
    rem=num%10;
    s=rem**3
    flag=flag+s
    num=num//10

if(flag==n):
    print("Armstrong number")
else:
    print("Not armstrong")
'''
#linear search
'''
li=[1,3,4,6,2,-5,-6,-7]
found=0
num=int(input("Enter the number "))
for i in li:
    if li[i]==num:
        found=1
        print("value found")
        break
    else:
        found=0
if(found==0):
    print("value not found")
'''

#Binary Search
'''
li=[1,3,2,5,3,-3,-5]
num=int(input("Enter the number to search"))
found=0
l=0
h=5
for i in li:
    while(l<=h):
        mid=(l+h)//2
        if(li[mid]==num):
            found=1
            print("value found")
            break
        elif(li[mid]>num):
            h=mid-1
        else:
            l=mid+1
if(l>=h and found==0):
    print("Value not found")
'''

#function
'''
def sum(x,y):
    add=x+y
    return add
a=sum(10,20)
print(a)
'''

'''
def area(r):
    return 3.14*r*r
print(area(2))
'''

#pass statement: if we have to not give any statement
'''
def funt(x,y):
    pass
funt(10,20)
'''

#file handling
'''
f=open("myfile.txt","w")
f.write("Welcome to python")
f.close()

f=open("myfile","r")
print(f.read(10))
f.close()
'''
''' with open("myfile.txt","w") as f'''

#Creating  module
'''
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x//y

Now in next file
import used_module
a=used_module.add(10,20)
b=used_module.sub(20,10)
print(a,b)
'''

#creating array
'''
from array import *
val=array("i",[2,3,4,1])
for i in range(0,4):
    print(val[i])
'''

#taking value into array
'''
from array import *
val=array("i",[])
n=1
while(n<5):
    x=int(input("Enter the element"))
    val.append(x)
    n=n+1
print(val)
'''

#Bubble sort
'''
from array import *
val=array("i",[])
n=1
while n<5:
    x=int(input("Enter the number"))
    val.append(x)
    n=n+1
print(val)
#applying logic

for i in range(1,5):
    for j in range(1,5-i-1):  
        if(val[j]>val[j+1]):
            temp=val[j]
            val[j]=val[j+1]
            val[j+1]=temp
print(val)
'''

#Bubble sort
'''
li=[3,5,2,8,9]
for i in range(0,5):
    for j in range(5-i-1):
        if li[j]>li[j+1]:
            temp=li[j]
            li[j]=li[j+1]
            li[j+1]=temp
print(li)

for i in li:
    print(li,end="")
    break
'''

#insertion sort
'''
li=[4,3,6,1,2]
for i in range(1,6):
    while():
        temp=li[i]
        j=i-1
        if li[i]>li[j]:
            li[j+1]=li[j]
        li[j+1]=temp
print(li)
'''

#Inheritence
#1-single level inheritence
'''
class a:
    def fun1(self):
        print("This is fun1")
class b(a):
    def fun2(self):
        print("This is fun2")
obj1=a()
obj2=b()
obj1.fun1()
obj2.fun1() 
'''

#2-multiple inheritence
'''
class A:
    def area(self,h,w):
        self.height=h
        self.width=w
        print("height + width is:",height+width)
class B(A):
    def show(self):
        print("class B")
class C(B):
    def display(self):
        print("class C")

obj1=A()
obj2=B()
obj3=C()

obj1.area(10,20)
obj2.show()
obj3.display()

obj2.area(30,30)
obj3.show()
'''

#3-multiple inheritence
'''
class a:
    def fun1(self):
        print("fun1 called")
class b:
    def fun2(self):
        print("fun2 called")
class c(a,b):
    def fun3(self):
        print("fun3 called")
obj1=a()
obj2=b()
obj3=c()


obj3.fun1()
obj3.fun2()
'''

#4-hierchial inheritence
'''
class a:
    def fun1(self):
        print("fun1 called")
class b(a):
    def fun2(self):
        print("fun2 called")
class c(b):
    def fun3(self):
        print("fun3 called")
        
obj1=a()
obj2=b()
obj3=c()

obj2.fun1()
obj3.fun2()
'''

#constructor
'''
class A:
    def __init__(self):
        print("hi")
obj1=A()
'''
'''
class A:
    def __init__(self,h,w):
        self.height=h
        self.width=w
        print("height+width",self.height,self.width)

obj1=A(10,20)
'''

'''
try:
    num=int(input("Enter the number"))
    if 5%num:
        print(num)
except:
    print("Not equal")
finally:
    print("Yes last loop")
'''
'''
#tower of hanoi
def toh(n,a,b,c):
    if n==1:
        print("move disc",n,"from",a,"to",c)
    else:
        toh(n-1,a,c,b)
        print("Move disc",n,"from",a,"to",c)
        toh(n-1,b,a,c)
toh(3,'a','b','c')
''' 




