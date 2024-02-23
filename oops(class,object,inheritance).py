#Basic Class and Object
#Create a car class with attributes like brand and model.Then create an instance of this class.
# class Car:
#   def __init__(self,brand,model):
#     self.brand=brand
#     self.model=model
  
#   def full_name(self):
#      return f"{self.brand} {self.model}"

# my_Car=Car("Hyundai","I20")  
# print(my_Car.brand)
# print(my_Car.model)

# my_newCar=Car("TaTa","safari")
# print(my_newCar.model)
# print(my_newCar.brand)
# print(my_Car.full_name())

#Class Method and Self
#Add a method to the Car class that displays the full name of the car (brand and model).
class Car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  
  def full_name(self):
     return f"{self.brand} {self.model}"
  
  def model_wheels(self,wheelname):
     self.wheelname=wheelname
     return f"{self.wheelname}"


my_newCar=Car("Tata","safari")
print(my_newCar.full_name())
print(my_newCar.model_wheels("MRF"))

#Inheritance
#Create an Electric car class that inherits from the Car class and has an additional attribute battery_size

class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size=battery_size
my_tesla=ElectricCar("Tesla","Model S","85KwH")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.full_name())


      
   