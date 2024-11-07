
#inheritence:-  inherits the properties from parent class to the child class.
 
# types of inheritence:-

# 1.sigle inheritence:- 
#  a child class inherits properties and methods from a single parent class.

# Ex:-

class Samsung:
    company = "Samsung"
    website = "www.samsung_india.com"

    def contact_deails(self):
        print("address : Bangaluru")

class Samsung_A55(Samsung):
    def __init__(self):
        self.name = "Samsung_A55"
        self.year = 1998

    def product_details(self):
        print("name : ",self.name)
        print("year : ", self.year)
        print("company : ", self.company)
        print("website : ", self.website)

mobile = Samsung_A55()
mobile.product_details()
mobile.contact_deails()
print("--------------------------------")


#2.multiple inheritence:- 
# a class to inherit attributes and methods from more than one parent class.

#Ex:-

class Worker:
    def do_work(self):
        print("Doing work")
 
class Manager:
    def manage(self):
        print("Managing the team")
 
class Employee(Worker, Manager):
    def perform(self):
        print("Performing employee duties")
 
employee = Employee()
employee.do_work()  
employee.manage()  
employee.perform()
print("------------------------------")
 
#3.hierachical inheritence:-
#  inheriting properties and method from single class from multiple class at a same time.

#EX:-

class Shape:
    def draw(self):
        print("Drawing a shape")
 
class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius
 
class Rectangle(Shape):
    def area(self, length, width):
        return length * width
 
class Square(Rectangle):  
    def area(self, side):
        return side * side
 
circle = Circle()
rectangle = Rectangle()
square = Square()
circle.draw()  
print("Circle Area:", circle.area(5))
rectangle.draw()  
print("Rectangle Area:", rectangle.area(5, 10))  
square.draw()  
print("Square Area:", square.area(4))
print("----------------------------")
 
#4.hybrid inheritence:- 
# using more then one type of inheritence.

#Ex:-

class Device:
    def power_on(self):
        print("Device powered on")
 
class Phone(Device):
    def make_call(self):
        print("Making a call")
 
class SmartPhone(Phone):
    def browse_internet(self):
        print("Browsing the internet")
 
class Laptop(Device):
    def run_program(self):
        print("Running program")
 
class SmartLaptop(Laptop):
    def video_call(self):
        print("Making a video call")
 
 
smartphone = SmartPhone()
smartphone.power_on()
smartphone.make_call()  
smartphone.browse_internet()  
 
smartlaptop = SmartLaptop()
smartlaptop.power_on()  
smartlaptop.run_program()
smartlaptop.video_call()  




