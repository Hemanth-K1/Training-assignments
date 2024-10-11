"""task5. Mathematical Operations:
1.Create two lists of numbers, and use the + operator to concatenate them. Then, use the * operator to repeat the elements of one list 3 times.
2.Given a list of numbers, write a Python program to create a new list where each element is doubled (i.e., each element is multiplied by 2).
"""
list1 = [1,2,3]
list2 = [4,5,6]

modified_list = list1 + list2 
print(modified_list)

repeated_list = list1 * 3 
print(repeated_list)

numbers = [11,12,13,14,15,16,17]

double_list = [num * 2 for num in numbers]
print("Double list: ",double_list)  