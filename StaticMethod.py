#Add a static method to the Car class that returns a general description of a car.

class Car:
  def __init__(self,brand,model):
    self.__brand=brand    #Here, __ we private the brand using double underscore.
    self.model=model
  def get_brand(self):
     return self.__brand + " !"  # here, brand is private.
  
  def full_name(self):
     return f"{self.__brand} {self.model}"  #here, brand is private.
  
  def model_wheels(self,wheelname):
     self.wheelname=wheelname
     return f"{self.wheelname}"
  
  #Here,Static Method not self is used in the method that is genearl_description(self) not allowed.
  @staticmethod
  def general_description():
     return "Car are means of transport"


my_newCar=Car("Tata","safari")
Car("Baba-RamDev","Kalyug-500")
print(my_newCar.full_name())
print(my_newCar.model_wheels("MRF"))


print(my_newCar.general_description())
print(Car.general_description())


      
   