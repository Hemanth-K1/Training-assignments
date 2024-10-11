"""task4. Aliasing and Cloning:
1.    Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list.
2.    Write a Python program to demonstrate how changes in a list's alias affect both lists,while changes in a cloned list do not.
"""

l1 = [1,2,3,4,5]
alias_list = l1 
l1.append(6)

print(l1)
print(alias_list)

cloning_list = l1.copy()
cloning_list.append(7)

print(l1)
print(cloning_list)