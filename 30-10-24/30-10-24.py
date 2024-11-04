# classmethod:- The classmethod decorator in Python is used to defi ne a class method.
# decorator :- Decorators in Python are a way to modify or enhance the behavior of functions or classes without directly modifying their source code.
# static variable :- When we declare a variable inside a class but outside method is called static variable.

class Employee:
    company="skywaves softwares"
    def getdetails(self):
        self.ename=input("enter employee name : ")
        self.eid = int(input("enter employee id : "))
        self.esalary = int(input("enter employee salary : "))
        self.desig = input("enter employee designation : ")

    def empdetails(self):
        print("Employee name : ", self.ename)
        print("Employee id : ", self.eid)
        print("Employee Salary : ", self.esalary)
        print("Employee designation : ", self.desig)
e1 = Employee()
print(e1)
e1.getdetails()
e1.empdetails()

e2 = Employee()
print(e2)
e2.getdetails()   
e2.empdetails()



# Write a program to  get student details?
class college:
    college_name= "Global academy of technology"
    def __init__(self,):
        self.sname = str(input("Enter the student name : "))
        self.sid = int(input("Enter the student USN number : "))
        self.sbranch = str(input("Enter the branch : "))
        self.saddress =str(input("Enter a address : "))

    def studentdetails(self):
        print("Student Name : ", self.sname)
        print("Student id : ", self.sid)
        print("Student Branch : ", self.sbranch)
        print("Student Address : ", self.saddress)

s1=college()
print(s1)
s1.studentdetails()
