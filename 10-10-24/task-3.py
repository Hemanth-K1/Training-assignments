"""task3. Sorting and Reversing Lists:
1.   Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse().

2.   Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results."""



list_1 = [1,7,3,6,9,6,5]
list_1.sort(reverse=True)
print(list_1)
print("---------------------------")


list_1.sort()
print(list_1)
print("---------------------------")



list_1.reverse()
print(list_1)
l1 = ["anil","rahul","asha","rakul"]
l1.reverse()
print(l1)
print("-----------------------------")


result = l1[::-1]
print(result)
print(l1 == result)