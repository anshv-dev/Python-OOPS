#Polymorphism(Different classes can have same method function example->fuel_type())
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
  
  def fuel_type(self):
     return "Petrol or Diesel"


my_newCar=Car("Tata","safari")
print(my_newCar.full_name())
print(my_newCar.model_wheels("MRF"))



class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size=battery_size

   def fuel_type(self):
     return "Electric Charge"   
my_tesla=ElectricCar("Tesla","Model S","85KwH")

print(my_tesla.fuel_type())

safari=Car("Tata","Safari")
print(safari.fuel_type())

print(my_newCar.fuel_type())

      
   