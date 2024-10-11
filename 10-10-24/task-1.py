"""1.Write a Python program to create a list of 5 integers and print the sum of all
     elements in the list.
2.   Create a list of strings containing the names of 5 fruits. 
     Access and print the second and fourth elements using indexing.
3.   Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, 
     the last three numbers, and every second number in the list."""


list = [1,2,3,4,5,10,20]
result = sum(list)
print(result)



list = ["Banana","mango","orange","kiwi","graps","apple"]
print("first fruit: ",list[2])
print("fourth fruit: ",list[5])



numbers = [1,2,3,4,5,6,7,8,9,10]
print("first three number:",numbers[:3])
print("last three number:",numbers[-3:])
print("every second number:",numbers[1::2])