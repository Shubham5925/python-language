#constructor: - when the user does not call the funt. with their arguments then it automatically gives some default values.
#automatically called when the class is executed and object is created
'''
1-parameterized constructor- argument constructor
2-non parameterized constructor-default constructor
'''

'''
class xyz:   
    def __init__(self,n,a):   #argument constructor
        self.name=n
        self.age=a
    def display(self):
        print("constructor called :",self.name,self.age)

obj1=xyz("shubham",19)
print(obj1.display())
'''

'''
class xyz:   
    def __init__(self):   #deafult constructor:- whatever is written all will always executed
        print("default constructor")
        
    def display(self):
        print("default constructor called :")

obj1=xyz()
print(obj1.display())
'''

