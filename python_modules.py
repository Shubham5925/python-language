#Modules: modules are the .py files in which it contains a block of code and we import into another file and call the sepecific function
'''
Modules are of two types:-
1-build-in mudules ex-import platform , and system method
2-user defined modules


ex-build-in mudules
import platform     #This is build -in module
x=platform.system()
print(x)    #prints output -windows


ex-dir() :-build-in module
import platform
x=dir(platform)
print(x)
'''


#2-below is user defined modules
def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y
