#Encapsulation
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


my_newCar=Car("Tata","safari")
print(my_newCar.full_name())
print(my_newCar.model_wheels("MRF"))


class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size=battery_size
my_tesla=ElectricCar("Tesla","Model S","85KwH")
# print(my_tesla.__brand) Here,by using double underscore brand name cannot be accessed by the object that is why encapsulation is used.
print(my_tesla.model)
print(my_tesla.full_name())

#Encapsulation->
#Modify the Car class to encapsulate the brand attribute, making it private and provide a getter method for it.
print(my_tesla.get_brand())


      
   