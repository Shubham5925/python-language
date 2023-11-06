#Types of argument
'''
1-keyword argument
2-positional argument
3-default argument
4-variable length argument
'''
'''
1-keyword argument
def my_function(num1,num2,num3):
    print("Third number is:",num3)

my_function(num1=10,num2=20,num3="Thirty")
'''

'''
2-default argument
def my_function(country="norway"):
    print(country)

my_function()   #here i have not passed the argument so by default "norway" is getting printed
'''

'''
3-arguments argument (*):if no of parameter is unknown and we need to enter the tuple
def my_function(*num):      #if we do not know how many arguments will be passed to the function so we use " * "
    print(num)

my_function(1,"one",2,"two",3,"three")
'''

'''
4-arguments argument (**):if no of parameter is unknown and we need to enter the dictionary
def my_function(**num):      #if we do not know how many arguments will be passed to the function so we use " ** " for dictionary
    print(num["lname"])

my_function(fname="shubham",lname="singh")
'''




















