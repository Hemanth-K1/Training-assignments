
#4. Hierarchical Inheritance

#2.Problem Statement: Create a base class Vehicle with attributes brand and model. Then, create two derived classes Car and Bike, both inheriting from Vehicle, and adding their own attributes and methods.

'''Tasks:
Define a base class Vehicle with attributes brand and model.
Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
Create another derived class Bike that inherits from Vehicle and adds an attribute type.
Implement methods to display the details of the vehicles.
Create instances of both Car and Bike and display their information.'''

class Vehicle:
    def __init__(self):
        self.brand = input("Enter Vehicle Brand Here : ")
        self.model = input("Enter Vehicle Model Here : ")

    def vehicle_details(self):
        print("Vehicle Brnd : ", self.brand)
        print("Vehicle Model : ", self.model)

class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.num_doors = input("Enter No.of Doors : ")

    def car_details(self):
        self.vehicle_details()
        print("Number Of Doors : ", self.num_doors)

class Bike(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.Type_bikes = input("Enter Type Of Motercycle here : ")

    def bike_details(self):
        print("Bike Type : ", self.Type_bikes)


c=Car()
c.car_details()

b=Bike()
b.bike_details()




#5. Hybrid Inheritance
#Problem Statement: Create a class structure to represent hybrid inheritance:

'''Device: Base class with name attribute.
Phone: Derived from Device with an additional phone_number attribute.
Tablet: Derived from Device with an additional screen_size attribute.
Smartphone: Derived from both Phone and Tablet with an additional attribute os.

Tasks:
Define a base class Device with an attribute name.
Define a class Phone that inherits from Device and adds an attribute phone_number.
Define a class Tablet that inherits from Device and adds an attribute screen_size.
Define a class Smartphone that inherits from both Phone and Tablet, adding an attribute os.
Implement methods to display all attributes of the Smartphone.
Create an instance of Smartphone and display its information.'''


class Device:
    def __init__(self):
        self.name = input("Enter Device Name Here : ")

    def device_details(self):
        print("Device Name : ", self.name)

class Phone(Device):
    def __init__(self):
        Device.__init__(self)
        self.phone_number = int(input("Enter Phone Number Here : "))

    def phone_details(self):
        print("Phone Number : ", self.phone_number)

class Tablet(Device):
    def __init__(self):
        self.screen_size = float(input("Enter Screen Size Here : "))

    def tablet_details(self):
        print("Screen Size : ", self.screen_size)
    
class Smartphone(Phone,Tablet):
    def __init__(self):
        Phone.__init__(self)
        Tablet.__init__(self)
        self.os = input("Enter Os Here : ")

    def smartphone_details(self):
        print("OS : ", self.os)
    

s=Smartphone()
print('-'*30)
s.device_details()
s.phone_details()
s.tablet_details()
s.smartphone_details()


#6.Basic Inheritance
#Problem Statement: Create a class Person with attributes: name and age. Create another class Student that inherits from Person and has an additional attribute grade. Define methods in both classes to display the attributes.
''''
Tasks:
Define a Person class with an __init__ method to initialize name and age.
Define a Student class that inherits from Person, with an additional attribute grade.
Define a display_info method in both Person and Student classes to print all attributes.
Create objects for both Person and Student and display their information.
'''

class Person:
    def __init__(self):
        self.name = input("Enter Name Of Person Here : ")
        self.age = int(input("Enter Person Age Here : "))
    
    def person_details(self):
        print("Person Name : ", self.name)
        print("Person Age : ", self.age)
    
class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.grade = input("Enter Student Grade Here : ")

    def student_details(self):
        self.person_details()
        print("Student Grade : ", self.grade)

s=Student()

print('-'*30)

s.student_details()


#Data Abstracion:-  used to hide unnecessary information and display only necessary information to the users interacting.

#1. Abstract Classes: These are classes that cannot be instantiated directly and may contain abstract methods that must be implemented by subclasses. You can create abstract classes using the abc (Abstract Base Class) module.
 
 
#2. Abstract Methods: Methods in an abstract class that have no implementation. They must be overridden in any subclass.


from abc import ABC, abstractmethod

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        pass
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Available")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()
car1.sunroof()

