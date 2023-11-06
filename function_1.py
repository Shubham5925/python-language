#creating function : Using def keyword

'''passing list as an argument'''
'''
def my_function(list1):   #function prototype
    for i in list1:                     #function definition
        print(i)

l1=[1,2,3,4,5,6]
my_function(l1)         #function calling
'''

#returning function value
'''def sum(x,y):
    return x+y

print(sum(10,20))
'''

#function are of 4 types
'''
1-without argument without return type
2-without argument with return type
3-with argument with return type
4-with argument with return type
'''


#eg- with return type without argument
'''
def list1():
    x=200                    # a function can have only single return type
    return "list"
    return x
 
print(list1())
'''
#pass statement:pass statement is the statement which help us to remove erroe in case of non-definition function 
'''
def my_function():         #gives no error
    pass
    
my_function()
'''
'''
def my_function():         #gives error :- function definition is not present
    pass
    
my_function()
'''










