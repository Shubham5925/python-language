#File handling in python
'''
steps for file handling
1-read 2- write 3-close
mode of opening
r,a,w,t,b,r+,w+

w-used to create new file and if the same file name exists then it does not gives error
a-append used to add contents/write over the previous data
x- used to create new file and if the file exists it gives error
'''

'''
f=open("myfile.txt","w")
f.write("hello python")
f.close()

f=open("myfile.txt","r")
print(f.read(20))
f.close()

f=open("myfile.txt","a")
f.write("Welcome to the world of python")
f.close()

f=open("myfile.txt","r")
print(f.read(100))
print(f.readline())
f.close()

import os    #os is module and os.remove is the function
os.remove("myfile.txt")
'''
