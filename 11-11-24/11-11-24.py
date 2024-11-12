"""-Polymorphism:- It refers to the use of a single type entity (method, operator or objet to represent different types in different scenarios.

-Method overloding:- Two or more methods have the same name but different numbers of parameters or different types of parameters.

-method overriding:-  when you have two methods with the same name that each perform different tasks"""

# Ex:-
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car_1 = Car("BMW", "Breza")     
boat_1 = Boat("Seaways", "Waterway") 
plane_1 = Plane("Airindia", "Airbus")    

for x in (car_1, boat_1, plane_1):
  x.move()