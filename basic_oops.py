#Python classes and objects
'''
Python is an object oriented programming which means that it has 4 pillars
1-abstraction
2-encapsulation
3-polymorphism
4-inherience

Almost everything in python is in the form of classes and objects

Classes :- It is the combination of Data member+Member function
Objects :- Objects are real world entities. objects also contains methods.

We use class keyword to create class

ex-creating class
class myclass:
    x=10


ex-creating object of the classes
class myclass:
    x=10

obj1=myclass()
print(obj1.x)


'''

#_init_() function :-
'''
-It is build in _init_ function , a kind of specia function
-whenever the classes are being executed the _init_function are called always
-it is assigned because to provide the important operations to be performed
when the classes are executed , and objects arae created.


ex-_intit_() fuction used

class person:
    def __init__(self,age,name):
        self.name=name
        self.age=age

obj1=person()
print(obj1.name)
print(obj1.age)

_init_ funt. is called automatically as the class is executed and object is
created
'''

'''
#ex-
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunction(self):
        print("hello"+self.name)


obj1=person("John",36)
obj1.myfunction()
'''


#self :-
'''
self parameter is the reference variable reffered to the current
instance of the class, and is use to access variables that belongs
to class.
'''


























