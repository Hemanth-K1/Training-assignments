
#list:-
#list is a collection of data types. it holds the group of values
# list is a mutable object. 
#list allow duplicates.
#list can also created by using list() function.

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

#List Operation:-

#LEN():- Return length of list.
#ex:-
lo=[1,2,3,4,5,6]
print(len(lo))
print('-----------------------------')

#concatenation:- Join two lists.

lo1=["banana","apple"]
print(lo+lo1)
print('--------------------------')

#repetition:- Repeats elements in list.

print(lo1*2)
print('------------------------------')

#in:- checks if the value is present in the list.

print(4 in lo)
print('------------------------------')

print(10 in lo)
print('------------------------------')

#not in :-checks if the value is present in the list.
print(10 not in lo)
print('------------------------------')

print(4 not in lo)
print('------------------------------')

#max:- returns maximum value in the list.

print(max(lo))
print('------------------------------')

#min:- returns minmum value in the list

print(min(lo))
print('------------------------------')

# sum:-add the values in the list that has nubers.
# ex:-
print(sum(lo))
print('------------------------------')

# all:- returns true if all elements of list are true (or if the list is empty).

print(all(lo))
print('------------------------------')

# any:- returns true if any element of the list is true, if list is empty it returns false.

print(any(lo))
print('------------------------------')

#list:- converts an iterable (tuple, string, set, dictionary) to a list.

list1=list("hello")
print(list1)
print('------------------------------')

#sorted:-returns a new sorted list.the original list is not sorted.

list2=[5,9,4,6,1,2]
list3=sorted(list2)
print(list3)
print('------------------------------')
