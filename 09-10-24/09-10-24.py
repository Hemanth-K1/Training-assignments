#list methods:-
# append():-
# ex:-appends an element to the list.
lm=[1,2,3,4,5,6,7,3,5,5,2,1,2,6,6,3,1,]
lm.append(10)
print(lm)
print('--------------------------------')

#count():-count the numbers of times an element appears in the list.

print(lm.count(2))
print('--------------------------------')

#index():-return the lowest index of in the list.

print(lm.index(1))
print('--------------------------------')

#insert():-insert object at the specified index in the list.

print(len(lm))
lm.insert(17,10)
print(lm)
print('--------------------------------')

#pop():-removes the elements at the specified index from the list

lm.pop()
print(lm)
print("------------------------------")

# rmove():-remove or delect object from list.

lm.remove(5)
print(lm)
print('--------------------------------')

#reverse():- reverse the element of the list.

lm.reverse()
print(lm)
print('--------------------------------')

#sort():- sort the element of the list.

lm.sort()
print(lm)
print('--------------------------------')

#extend():-adds the elements in a list to the end of anoter list.

lm2=["apple","water melon","cherry","banana"]
lm.extend(lm2)
print(lm)

#clear():-

lm.clear()
print(lm)
print('--------------------------------')
'''
#delete():-
#ex:-
del(lm)
print(lm)
print('---------------------------')
'''

# exaple:-
# write a progeram that creates a list of numbers from 1-20 that are eiher divisible by 2 or 4 without using the filter function.?
divi_2_4=[]
for i in range(2,22):
    if(i%2==0 or i%4==0):
        divi_2_4.append(i)
print(divi_2_4)
print('---------------------------------------')

# write a progeram that creates a list of numbers from 1-30 that are eiher divisible by 3 or 5 without using the filter function.?
divi_3_5=[]
for i in range(3,33):
    if(i%3==0 or i%5==0):
        divi_3_5.append(i)
print(divi_3_5)
print('---------------------------------')

# write a progeram that creates a list of numbers from 1-10 that are eiher divisible by 3 without using the filter function.?
divi_3=[]
for i in range(1,100):
    if i%3==0:
        divi_3.append(i)
print(divi_3)
print('-----------------------------------')

# write a program to list of 3 cubes.?
cubes=[]
for i in range(11):
    cubes.append(i**3)
print(cubes)
