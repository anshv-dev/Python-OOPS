#ClassVariables
class Car:
  total_car=0    # Adding counter variable.
  def __init__(self,brand,model):
    self.__brand=brand    
    self.model=model
    Car.total_car+=1    # Incrementing the counter Variable.   
  def get_brand(self):
     return self.__brand + " !"  
  
  def full_name(self):
     return f"{self.__brand} {self.model}" 
  
  def model_wheels(self,wheelname):
     self.wheelname=wheelname
     return f"{self.wheelname}"
  
  def fuel_type(self):
     return "Petrol or Diesel"

safari=Car("Tata","Safari")
AudiCar=Car("Audi","B-500")
my_newCar=Car("Tata","safari")
print(my_newCar.full_name())
print(my_newCar.model_wheels("MRF"))

print(safari.fuel_type())

print(my_newCar.fuel_type())
print(Car.total_car)
      
   