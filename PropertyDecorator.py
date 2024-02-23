#Use a property decorator in the Car class to make the model attribute read only

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
  



my_newCar=Car("Tata","safari")
# my_newCar.model="City" #Here, we have changed the model name.

#using property decorator you can use model rather than model()
print(my_newCar.model)

      
    