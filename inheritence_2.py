#types of inheritence
'''
1-single level inheritence
2-multi-level inheritence
3-multiple inheritence
4-hierchial inheritence
5-hybrid inheritence
'''

#1- single level inheritence :one parent class inherits into one child class
'''
class a:
    def display(self):
        print("display method from parent class:-")

class b(a):
    def show(self):
        print("show method from base class")

obj1=a()
obj1.display()

obj2=b()
obj2.show()
obj2.display()
'''

#2-multi-level inheritence
'''
class a:
    def display(self):
        print("display method from class a (parent class)")
    
class b(a):
    def show(self):
        print("show method from class b (child class)")   

class c(b):
    def visible(self):
        print("visible method from class c(child class)")

obj1=a()
obj2=b()
obj3=c()

obj2.display()
obj3.show()
obj3.display()
'''

#3-multiple inheritence: - inheriting property of multiple class into one class ,python supports multiple inheritence
'''
class a:
    def display(self):
        print("display method from class a (parent class)")
    
class b:
    def show(self):
        print("show method from class b (child class)")   

class c(a,b):   
    def visible(self):
        print("visible method from class c(child class)")


obj3=c()
obj3.display()
obj3.show()
'''


#4- hierchial inheritence : inherits one parent class into many base classes
'''
class a:
    def display(self):
        print("display method from class a (parent class)")
    
class b(a):
    def show(self):
        print("show method from class b (child class)")   

class c(a):
    def visible(self):
        print("visible method from class c(child class)")

obj2=b()
obj2.display()

obj3=c()
obj3.display()
'''

#5-hybrid level inheritence: combination of any two above inheritence-, here single+multilevel
'''
class a:
    def display(self):
        print("display method from class a (parent class)")
    
class b(a):
    def show(self):
        print("show method from class b (child class)")   

class c(b):
    def visible(self):
        print("visible method from class c(child class)")

obj1=a()

obj2=b()
obj2.display()

obj3=c()
obj3.show()
'''










    

