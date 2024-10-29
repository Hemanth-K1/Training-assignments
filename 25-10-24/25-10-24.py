
'''What is python?
Python is a high-level, interpreted, interactive, object-oriented, dynamically typed, and reliable language that is very simple and uses English-like words. It has a vast library of module to support integration of complex solution from pre-built components
Python application:-
BitTorrent….
You tube….
Dropbox…
Deluge…
Cinema 4D…
3D Software…
Games…
Why python?
Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax like the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way, or a functional way.
Why it is called 'python'?
	Python language was released its designer, Guido Van Rossum, in February 1991.He was reading  the published scripts from Monty python’s Flying Circus. He was fan of the show he thought python would be the prefect name for the new language 
Features of python?
Easy To Learn and Readable Language. Python is extremely easy to learn. ...
Interpreted Language. ...
Dynamically Typed Language. ...
Open Source and Free. ...
Large Standard Library. ...
High-Level Language. ...
Object Oriented Programming Language. ...
Large Community Support. 
Advantage of python?
Simple to Use and Understand. For newcomers, Python is simple to understand and use. ...
Free and Open-Source. Video Player is loading. ...
Productivity has Increased. ...
Interpreted Language. ...
Extensive library. ...
Dynamically Typed. ...
Portability. ...
Supportive community.
'''
'''
Operators:
Operators are used to perform operations on variables and values.
Various operators supported by Python are:
1.Arithmetic operators
2.Comparision operators
3.Logical operators
4.Assignment operators
5.Identity operators
6.Membership operators
7.Bitwise operators
1.Arithmetic operators: for performing Arithmetic operations.
Various Arithmetic operators are:
1.Addition(+) :- adds two operands.
2.Subtraction(-) :- subtracts two operands.
3.Multiplication(*) :- multiplies two operands.
4.Division(/) :- divides the first operand by the second.
5.Floor Division(//) :- divides the first operand by the second.
6.Modulo Division(%) :- returns the remainder when the first operand is divided by the second.
7.Exponent(**) :- Returns first raised to power second.
'''
#Ex:-
x=10
y=4
add=x+y
print("sum=",add)
sub=x-y
print("diff=",sub)
mul=x*y
print("product=",mul)
div=x/y
print("Division=",div)
#Ex:-
floordiv=x//y
print("Floordivision=",floordiv)
moddiv=x%y
print("moddiv=",moddiv)
exp=x**y
print("exp=",exp)
'''
2.Comparision operators:- Comparison operators are used to compare two values. Comparison operators always returns either True/False
== :- True if both operands are equal.
!= :- True if operands are not equal.
>= :- Greater than or equal to True if the left operand is greater than or equal to the right.
<= :- Less than or equal to True if the left operand is less than or equal to the right.
> :- True if the left operand is greater than the right.
< :- True if the left operand is less than the right.
'''
#Ex:-
x=10
y=4
print(x>y)
print(x<y)
print(x>=y)
#Ex:-
x = 5
y = 3
print(x <= y)
print(x > y)
print(x < y)
#3.Logical operators:- Logical operators are used to combine conditional statements.
#AND :- True if both the operands are true.
#OR :- True if either of the operands is true.
#NOT :- True if the operand is false.
#Ex:-
x = 5
print(x > 3 and x < 10)
#Ex:-
x = 9
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))
'''
#4.Assignment operators:- Assignment operators are used to assign values to variables. Assignment operators are also called as short-hand operators.
= :- Assign the value of the right side of the expression to the left side operand.
+= :- Add right-side operand with left-side operand and then assign to left operand.
-= :- Subtract right operand from left operand and then assign to left operand.
*= :- Multiply right operand with left operand and then assign to left operand.
/= :- Divide left operand with right operand and then assign to left operand.
%= :- Takes modulus using left and right operands and assign the result to left operand.
//= :- Divide left operand with right operand and then assign the value(floor) to left operand.
**= :- Calculate exponent(raise power) value using operands and assign value to left operand.
&= :- AND on operands and assign value to left operand.
|= :- OR on operands and assign value to left operand.
^= :- XOR on operands and assign value to left operand.
>>= :- Performs Bitwise right shift on operands and assign value to left operand.
<<= :- Performs Bitwise left shift on operands and assign value to left operand.
'''
#Ex:-
x = 5
x += 3
x -= 3
x *= 3
x /= 3
x%=3
print(x)
print(x)
print(x)
print(x)
print(x)
print(x)
#Ex:-
x = 10
x//=6
x **= 6
x &= 6
x |= 6
x ^= 6
x >>= 6
x <<= 6
print(x)
print(x)
print(x)
print(x)
print(x)
print(x)
print(x)
'''
5.Identity operators :- These operators are used to compare the addresses of 2 objects.
Identity operators are,
  Is :- Returns True if both variables are the same object.
  is not :- Returns True if both variables are not the same object.
'''
#Ex:-
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) 	# returns True because z is the same object as x.
print(x is y)	# returns False because x is not the same object as y, even if they have the same content.
#Ex:-
x = ["car", "bus"]
y = ["car", "bus"]
z = x
print(x is not z)
print(x is not y)
'''
6.Membership operators:- These operators are used to check whether an element is present or not.
Membership operators are:
  In :- Returns True if a sequence with the specified value is present in the object.
  not in :- Returns True if a sequence with the specified value is not present in the object.
'''
#Ex:-
x = ["apple", "banana"]
print("banana" in x)
#Ex:-
x = ["kowshik", "ajay"]
print("veeru" not in x)
'''
7.Bitwise operators:- Bitwise operators are used to compare (binary) numbers.
AND (&) :- Sets each bit to 1 if both bits are 1.
OR ( | ) :- Sets each bit to 1 if one of two bits is 1.
XOR( ^ ) :- Sets each bit to 1 if only one of two bits is 1.
NOT ( ~ ) :- Inverts all the bits.
LIFT SHIFT ( << ) :- Shift left by pushing zeros in from the right and let the leftmost bits fall off.
RIGHT SHIFT ( >> ) :- Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost 
bits fall off.
'''
#Ex:-
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
#Ex:-
print( ~5)
print(3 << 2)
print(8 >> 2)
#Data types:-
#Date typer are two types
#Fundamental data types
#Collection data types
#Fundamental data types:-
#i)int :- A python int() function convert the specified value into an integer number.
#Ex:-
A=5
print(type(A))
#ii)float :- The float data type represents a floating point or decimal number.
#Ex:-
A=5.0
print(type(A))
#iii)complex :- The complex data type in python consists of two values , the first one is the real part of the
#		complex number, and the second one is the imaginary part of the complex number.
#Ex:-
(3+7j)
#iv) Boolean:- Python Boolean type is one of the bult-in data types provided by python .which represents
#		one of the two value  i.e., true (or) false. 
#Ex:-
X=200
Y=33
print(X>Y)
#v) String data type:- A string is a collection of one or more characters put in a single quotes , double quotes, and triple quotes. It is represented by “str” .the string is immutable, so its values cannot be changed.
#String methods:-
#Capitalize:- Converts the first character to upper case.
#Ex: -
x ="india"
print(x.capitalize())
#Title():- For capitalizing the 1st character of each word in a string
#Ex:-
x ="India is my country"
print(x.title())
#Collection data types:-
'''
List:- List is a collection data type which holds grope of values.
List properties:-
List represented by using [ ]
List allows both homogeneous (similar) and heterogenous(dissimilar) elements.
Ex: -X=[10,20,30,40,50] homogeneous elements
        Y=[101,'kowshik,'30369,40,true] heterogenous elements
List allows duplicates 
Ex: - X= [10,20,30,40,50,10,20,30]
In section order is followed i.e., the order in which the elements are inserted in the same order they are stored or displayed
Ex: - X=[10,20,30,40,50]
Each element of list is identified or accessed by a unique index
List supports 2 types of indexes:
Positive index (or) Forword index
Negative index (or) backword index
Ex: - 
O	     1	       2	          3		4	5 --- positive (or) Forword index
P	Y	T	H	O	N
                                                                                           
		
			-6	   -5           -4             -3            -2            -1  -- negative (or) backword index
'''            
#Change the item value:-
#To change the value of a specific item, refer to the index number:
#declaring a list:-
l=[1,2,3,4,5,6,7]
print(l)
print(type(l))
#mearging of two list:-
l1=[1,3,2,4,5,6]
l2=['a','b','c','d',]
print(l1+l2)
print(l1+l2+[7,8])
#loop in list:-
x=[1,2,3,4,5,6,7]
for p in x:
    print(p)
    print(type(p))
#nested list:-
nl=[["rohit",50],["sachin",150],["dhoni",100],["uvaraj",70]]
print(len(nl))
for p in nl:
    print(p)
for p,q in nl:
    print("player",p)
    print("runs",q)
NL=[1,'a',"abc",[2,3,4,5],8.9]
i=0
while i<(len(NL)):
    print("NL[",i,"]= ",NL[i])
    i+=1
#list functions:-
lf=[1,5,4,6,7,10,43,45,866]
print(sum(lf))
print(max(lf))
print(min(lf))
print(sorted(lf))
print(sorted(lf,reverse=True))
#list slicing:-
ls=["apple","banana","cherry","water melon","bag","fan","car","mobile","box","bottle"]
print(ls)
print(len(ls))
print(ls[2])
print(ls[-5])
print(ls[1:5])
print(ls[-8:-3])
print(ls[0:10:2])
print(ls[-10:-1:3])
'''
TUPLE :- Tuple is a collection datatype which holds group of values.
Tuples are used to store multiple items in a single variable.
A tuple is an immutable object, which means it cannot be changed, and we use it to represent fixed collections of items.
Tuple is allowing duplicate values
Ex: - x=(10,20,30,40)
Elements of tuples are enclosed in parenthesis ( ) round brackets and are separated by commas.
Like list and string, elements of a tuple can be using index values.
 0  1   2   3   4   5  --- positive (or) Forword index
 P  Y   T   H   O   N                                                                                               
-6 -5  -4  -3  -2  -1  -- negative (or) backword index
Tuple = ( )						#empty tuple
Tuple = (1)						#tuple with single element
Tuple1 = (1,2,3,4,5)					#tuple of integers
Tuple2 = (“economics”,87,”accountancy”, 89.9)	#tuple of mixed data types
Tuple is an immutable object i.e.; changes and modifications are not allowed within a tuple but elements of a tuple can be either mutable or immutable
 ex: y=(101,"James",70890.70,[1,2,3])
 tuple can also be created by using tuple() function.
Tuple allows both homogenous(same datatype) and heterogeneous(different datatype) elements
ex:  x=(10,20,30,40,50)  			#homogenous elements
       y=(101,"James",70890.70,[1,2,3]) 	#heterogeneous elements
'''
#NOTE: - If there is only one element within a tuple then it is not tuple.
#Ex: -
#creating a tuple:
t=(1,2,True,5.345,"hari",3,2,4,4)
print(type(t))
print(len(t))
#creating a tuple using tuple() function:
t1=tuple(input("Enter the values: "))
print(t1)
print(type(t1))
print(len(t1))
#converting tuple items:
t2=input("Enter the values: ")
print(t2)
print(type(t2))
t2_1=tuple(t2)
print(t2_1)
print(type(t2_1))
#accessing tuple:
t3=tuple(input("Enter the value: "))
print(type(t3))
print(t3[2])
print(t3[-4])
#tuple slicing:
t4=("apple","banana","watermellon","cherry","mango","kiwi",1,2,3,4,5.43,"q","A","D","Q")
print(t4[0:])
print(t4[:-1])
print(t4[5:10])
print(t4[-13:-8])
print(t4[2:14:3])
print(t4[-13:-1:2])
print(t4[::-1])
print(t4[-1:])
'''
SET :- Set is a collection datatype which holds group of values.
Set represented by using curly braces{ }.
Set allows homogeneous & heterogeneous elements.
Set allows duplicates.
In set order is not preserved.
Set doesn't support indexing. 
Set cannot access using while loop and index.
Set can access the elements of a set using for loop.
Set is a mutable object , but elements of set should be immutable only.
Set can be created directly by allowed by using { } or by using set( )function.
Set within  a set is not allowed because set  set allowed only immutable within it.
We can perform mathematical operation on a set object.  
'''
#Ex:-
thisset = {"apple","banana","cherry"}
print(thisset)
#Ex:-
thisset = set("hello")
print(thisset)
# Union: it reyturns both sets.
s12_1={1,2,3,4,5}
s12_2={1,2,6,7,8,9,10}
s12=s12_1.union(s12_2)
print(s12)
#            (or)
s12=s12_1|s12_2
print(s12)
# Intersection : it returns common elements in both sets.
s13_1={1,2,3,4,5}
s13_2={3,4,5,6,7}
s13=s13_1.intersection(s13_2)
print(s13)
#           (or)
s13=s13_1&s13_2
print(s13)
# Difference : it returned set contains items that exist only in the first set, and not in both sets.
s14_1={1,2,3,4,5}
s14_2={3,4,5,6,7}
s14=s14_1.difference(s14_2)
print(s14)
#           (or)
s14=s14_1-s14_2
print(s14)
'''
DICTIONARY :- Dictionary is a collection data type which holds group of (key, values)
Ex: -
thisdict ={"brand":"Ford","model":"Mustang","year":1964}
print(thisdict)
Output: -
{''brad': 'ford', 'model':'mustang', 'year': 1964}
     KEY	         VALUES          K		  V		K	     V
Properties of a dictionary: -
Dictionary represented by using curly braces { }.
Keys and values can be either homogeneous or heterogeneous.
Keys cannot be duplicated, but values can be duplicated
Ex: -
Age=60  wight=60
Insertion order is not preserved.
Indexing/slicing is not supported
Dictionary is mutable object. Within a dictionary , we can both mutable and immutable types.
Dictionary can be created directly by using { } or by using dict( ) function.
To access a elements of a dictionary , if we pass the key, we will get the value
Ex: -
X[“age]-returns value 25
'''
# Create a dictionary :
dict_1={}
key=(input("Enter key here : "))
value=(input("Enter value here : "))
dict_1[key]=value
print(dict_1)
#               (or)
for iteam in range(3):
    key=(input("Enter key here : "))
    value=(input("Enter value here : "))
    dict[key]=value
print(dict)
dict_2={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
print(dict_2)
print(type(dict_2))
print(len(dict_2))
# Accessing the values of a dictionary
dict_3={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
print(dict_3["Kohli"])
print(dict_3["Ashwin"])
print(dict_3["Siraj"])
# Get keys :
dict4_1={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict4=dict4_1.keys()
print(dict4)
# Get Values :
dict5_1={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict5=dict5_1.values()
print(dict5)
