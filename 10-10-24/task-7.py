"""7. Nested Lists:
1.    Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3.
2.    Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade.
"""

matrix =[[1,2,3],
         [4,5,6],
         [7,8,9]]

element = matrix[1][2]
print("Element at row 2 , column 3: ",element)



students = [["anil",95],
            ["harish",94],
            ["pradeep",93]]

for s in students:
    name , grade = s 
    print(f"{name}:{grade}")
    