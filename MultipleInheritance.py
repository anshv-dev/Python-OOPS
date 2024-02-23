#Create two Classes Battery and Engine and let the ElectricCar class inherit from both , demonstrating multiple inheritance

class Car:
  def __init__(self,brand,model):
    self.__brand=brand    #Here, __ we private the brand using double underscore.
    self.__model=model

  def get_brand(self):
     return self.__brand + " !"  # here, brand is private.
  
  def full_name(self):
     return f"{self.__brand} {self.__model}"  #here, brand is private.
  
  
  @property  #Here,we have used the decorator.
  def model(self):
     return self.__model  #Created model method

  def model_wheels(self,wheelname):
     self.wheelname=wheelname
     return f"{self.wheelname}"
  

class Battery:
   def battery_info(self):
      return "This is battery"

class Engine:
   def Engine_info(self):
      return "This is Engine"
      
class ElectricCarTwo(Battery,Engine,Car):
   pass 

my_newTesla=ElectricCarTwo("Tesla","Model X")
print(my_newTesla.battery_info())
print(my_newTesla.battery_info())