
#Default argument : These allow you to set default values for parameters. If no value is provided, the default is used.


def myFun(x, y=65):
    print("x: ", x)
    print("y: ", y)

myFun(70)


#Keyword Arguments: Passing values by their names. 


def greet(arg_1, arg_2): 

    print(arg_1 + " " + arg_2) 

greet(arg_1="how are you", arg_2="Mr Hemanth") 

#Positional Arguments: Values can be passed without using argument names. These values get assigned according to their position. Order of the arguments matters here. 

def greet(arg_1, arg_2): 

    print(arg_1 + " " + arg_2) 

greeting = input() 

name = input()  

greet(greeting, name) 

#Variable-length Arguments: a feature that allows a function to accept a variable number of arguments in Python.


def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello','Hi', 'Welcome', 'to', 'India')

#1. Write a Python function to check whether a number falls within a given range.
def check_range(n):
    if n in range(1,20):
        print("yes, the number is within range")
    else:
        print("the number is out of range")
check_range(19)

#2. Write a Python function that accepts a string and counts the number of upper and lower case letters.


def count_letters(c):
    d={"Upper_case":0, "Lower_case":0}
    for s in c:
        if s.isupper():
            d["Uppwe_case"] +=1
        elif s.islower():
            d["Lower_case"] +=1
        else:
            pass
    print("Original string", c)
    print("number of upper case characters : ",d["Upper_case"])
    print("number of Lower case characters : ",d["Lower_case"])
    count_letters('MY Name Is Hemanth, I am Working In SKYWAVES software')

#3. Write a Python function that takes a list and returns a new list with distinct elements from the first list.


def unique_elements(e):

    u=[]
    for i in e:
        if i not in u:
            u.append(i)
    print(u)
e=[1,2,3,3,3,3,4,5]
unique_elements(e)


