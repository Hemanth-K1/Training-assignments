"""task8. Advanced Challenges:
1         .Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists: One containing only the even numbers. Another containing only the odd numbers.
2.Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).Given a list of tuples representing (name, age), sort the list by age in ascending order."""


numbers = list(range(1,21))
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even_numbers: ",even_numbers)
print("Odd_numbers: ",odd_numbers)




numbers = [10,20,10,5,3,5,2,20]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:

        unique_numbers.append(num)
print("Unique numbers: ",unique_numbers)