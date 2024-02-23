#Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar

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
  
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size=battery_size
my_tesla=ElectricCar("Tesla","Model S","85KwH")
print(my_tesla.get_brand())
print(my_tesla.model)
print(my_tesla.full_name())

print(isinstance(my_tesla,Car)) #Output->True
print(isinstance(my_tesla,ElectricCar)) #Output->Also, True because it inherits the property of Car

# my_newCar=Car("Tata","safari")
# my_newCar.model="City" #Here, we have changed the model name.

#using property decorator you can use model rather than model()
# print(my_newCar.model)

      
    