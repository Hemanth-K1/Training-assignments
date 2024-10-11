"""task6. Membership Operators:
1.        Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."
          Given a list of student name , check if "John" and "Sara" are in the list using the in operator."""

students = ["hemanth","shanthkumar","rahul","johny","anitha","sara"]

for name in ["johny","sara"]:
    if name in students:
        print(f"{name} found at position {students.index(name)}.")

    else:
        print(f"{name} not found at position")