#Inheritence :- transferring the property from one entity to another
'''
parent class/base class /super class
child class/ derived class/sub class
'''

'''
ex-
class parent:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

#now creating parent class object

obj1=parent("shubham","singh")
obj1.printname()
   '''

#super() function:-
'''
python also has a super function that will make
the child class inherit all the properties methods from its parent class.
'''

'''
ex-
class parent :
    def __init__(self,fname,lname): #always called when class is executed and object is created ,just like initializing datamember
        self.firstname=fname
        self.lastname=lname

    def display(self):
        print("hello "+self.firstname+self.lastname)    #here to connect we can use '+' or ','operator to connect with message

#now creating object of parent class
x=parent("shubham","singh")          #creating object of parent class and calling a specific display method
x.display()
'''



#ex- parent class and child class inheriting
#creating parent class
'''
class area:
    def __init__(self,h,w):
        self.height=h
        self.width=w

    def display(self):
        print("area of rectagle is:",self.height*self.width)

class volume(area):    #creating child class and inheriting all the properties and methods of parent class
    pass

#creating object of child class and then calling display method of parent class

obj2=volume(10,20)
obj2.display()
'''

#now creating __init__ function for child class :- so no longer the property of parent class into child class
#now making __init__ function for child class and it has its own data member initialized

#making parent class
'''
class parent:
    def __init__(self,h,w):
        self.height=h
        self.width=w

    def display(self):
        print("method called from parent class :",self.height,self.width)

#making child class

class child:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def show(self):
        print("method called from child class :",self.firstname,self.lastname)

#now creating seperate objects for parent and child class and lets trying to access method from different objects
 
obj1=parent(10,20)  #creating object of parent class
obj2=child("shubham","singh")  #creating object of child class

obj1.display()    #calling method from parent class through its object only
obj2.show()     #calling method from child class through its object only
'''

#now trying to call method through another objects : - will always give error
'''
obj2.display()
obj1.show()
'''










 















































