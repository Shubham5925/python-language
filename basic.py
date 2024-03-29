# Basics of python  :print,all,typecast,comparison,string,list,tuple,dictionary,set,frozenset ....
'''print("Result is:",25/5)
print("Result is:",25//5)
'''
#print statement used
'''print("Hello Python" ,end=" . ")
print("not next line ")
'''

# Using ''all'' keyword for fast execution of the code  as it checks for one time only ....
'''a=1
b=4
c=5
all = a==1 and b==4 and c==5
if all:
    print("Yes checked")
if all:
    print("Yes checked again")
else:
    print("Yes checked again")
'''


# 0.1+0.2==0.3  //this is not equal ......
'''
print("Only for this : ",0.1+0.2==0.3)           #this occur because its decimal conversion is not equal to 0.3
print("Only for this : " ,0.3+0.6==0.9)          #this occur because its decimal conversion is not equal to 0.9
print("For any : ", 0.4+0.5==0.9)                   #Its decimal conversion is equal to 0.9
print("For any : ", 0.7+0.6==1.3)                   #same as above two reason
'''

# assigning the same value to multiple variable and swapping in one line.....
'''
a=b=c=10
print(a,b,c)
a,b,c=c,b,a
print(a,b,c)
'''

# raising power y on x
'''
x=2
y=5
print("Exponent is :", x**y)
'''

# Type Casting //syntax:   x=int(13.25+4/2)
''' print(int(13.25+4/2)) '''

#output
'''print("hello\example\text")
print("hello\\example\\text.txt")  '''

# Some String functions are .............
'''
string="Welcome to python world 123 @ 2023"
print(string.capitalize())
print(string.length())  # Not working only for shell not for editor 
print(string.isalnum())      #checks alphabet+numbers
print(string.isalpha())       #checks olny alphabet
print(string.isdigit())         #checks only digits
print(string.isspace())      #checks space in the string
print(string.islower())      #checks is the string in lower case or not
print(string.isupper())     #checks  is the string in upper case or not
print(string.istitle())         #checks all first letter capital letter
print(string.lower())        #it will make whole string in lower case
print(string.upper())        #it will make whole string in upper case
print(string.title())           #makes full string first letter capital 
print(string[:10])              #string slicing -gives string before 10th index
print(string[15:])              #string slicing - gives string after 15ths index 
print(string[::6])               #prints all letters at 6th - 6th index gap
print(string[6::])               #prints all letters after 6th index
print(string[::-1])              #prints string in reverse order
print(string[2:10])            #print string between index 2 to 9 
print(string[-3:-10])         #print no string as no string lie between it  because reverse string does not print
print(string[-20:-3])         #print string between index -20 to -4   it exclude -3 index
print(string.swapcase())  #prints copy of string but returns uppercase into lowercases and vice-versa
print(string.lstrip(char))  #still working on
print(string.rstrip(char))  #still working on 
'''

#Lists in python
'''
li=['a','e','i','o','u',1,2,3,"one","two","three"]         #list with multiple datatypes
print(li)                                                                                 #printing list
print(li[8])                                                                            #printig list at direct index number
print(li[-3])                                                                           #printig list at direct index number
print(li[2:8])                                                                         #List slicing 
for i in li:                                                                                #seperating list items
    print(i)                                                                             
li.append("four")                                                               #add the single item at the end of list
print(li)
li[7]=4                                                                                     #changing list element
print(li)
del li[7]                                                                                   #Using 'del' keyword we delete element through index
print(li)
del li[5:8]                                                                               # Using 'del' keyword deleting elements through slicing
print(li)
#b=li                            wrong method to copy list to another variable
b=list(li)                      #Correct method to make copy of the list
print(b)
print(b.index('u'))        #Gives index position of the number/string
l1=[1,2,3]                        # List l1
l2=["one","two","Three"]  #List l2
l1.extend(l2)                         #Adding two list l1+l2 using extend keyword
print(l1)
l2.insert(0,"zero")              #Adding element at any index using 'insert' keyword
print(l2)
l2.pop(0)                               #'POP' keyword is used to delete element by index number
print(l2)
l2.remove("one")              #'REMOVE' keyword is used to delete element by element name
print(l2)
l1.clear()                               #'CLEAR' keyword is used to delete all elements of the list
print(l1)
print(l2.count("one"))     #count the no of occurence of the element but above i have deleted one . ' . 0
li.reverse()                            #reverse the list for any list element
print(li)
li.sort()                                   #Sort the list element of any data tpe
print(li)
'''

#Tuples -Only 5 opeartions are there : indexing,slicing,cmp(compare),len,max,min
'''tuple=("one","two","three" ,1,2,3,"@")
tuple2=(3,2,5,6,1,7,2)
print(tuple)         #printing tuple
print(tuple[2])     #tuple element at index 2
print(tuple[:5])    #tuple element before 5th index
print(tuple[2::])   #tuple element after 2nd index
print(len(tuple))  #calculate length of tuple
print(max(tuple2))  #gives max value in tuple but for similar datatype
print(min(tuple2))  #gives min value in tuple but for similar datatype
# t=3,   creating tuple by adding , after 3
li=["one","two","three",1,2,3]       #creating tuple from list
t3=tuple(li)
print(t3)
'''

#Dictinaries in python
'''
dic={1:"one",2:"Two",3:"three",4:"four"}        #simple dictionary
print(dic.values())                                                     #to access values
print(dic.keys())                                                       #to access keys
dict2={5:"number","a":"string",(1,2,3):"tuple"}         #dict with number,string,tuple
for key in dict2:                                                                       # from key we can access values
    print(key,":",dict2[key])
dict2['[1,2,3]']="List"                                                             #Adding key:value to exisiting dictionary
print(dict2)
#dict2.pop("new")          //gives keyword error as new does not exist
print(len(dict2))               #len method used to print length of dictionary
dict2.get("a")                    #gives values corresponding to key
dict2.items()                     #gives all key and values
dict2.clear()                       #clears the whole key and values
print(dict2.keys())           #After clear it gives null dictionary
dict1={1:"one",2:"two",3:"three"}    #1st dictionary
dict2={"name":"shubh","Roll no":35,"Section":"B2"}   #2nd dictionary
dict1.update(dict2)                 #adding 2nd dctionary to first one 
print(dict1)
'''

#set theory   :Elements cannot be duplicate ,Using curly braces,items are immutable,no index number so print all or use looping methods,output is random
'''
days={"monday","tuesday","wednesday","thursday","friday","saturday","sunday"}
print(type(days))     #type:set
for i in days:              #printing through loops
    print(i)
days.add("weeks:");    #adding elements into set :for single element
print(days)
days.update(["months","years"])  #adding elements to set using update method for : more than one element
print(days)
#removing elements method:discard,remove,pop,clear,update
discard - if element does not exist it does not give error while using discard keyword
remove - if element does not exist then it gives error while using remove keyword
pop - only removes last element of set
clear - delete all elements of the set
update - change set elements
'''
#Opeartions on set: Union/(|) , intersection/(&) , difference /(-) ; set comparion : >,<,==,>=,<= it returns true/false
'''
set1={"one","two","three","four","five","six"}
set2={"three","one","five"}
print(set1|set2)
print(set1.union(set2))
print(set1&set2)
print(set1.intersection(set2))
print(set1-set2)
print(set1.difference(set2))
print(set1>set2)
print(set1<set2)
print(set1==set2)
'''

#Frozen set : Frozenset elements are immutable and has no add,update,del,clear no any keyword
'''
frozenset=frozenset([1,2,3,"one","two","three"])
print(frozenset)
print(type(frozenset))
'''






