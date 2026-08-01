class Car:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):                                      #Inheritance
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)                  #using super() method for accessing the parent class Methods
        self.battery_size=battery_size

elec_Car=ElectricCar("Tesla", "Model Y", "84kwh")
print(elec_Car.full_name())
    
my_car=Car("Toyota","Camry")
print(my_car.brand)
print(my_car.model)

my_new_car= Car("Range Rover", "hghfg")
print(my_new_car.full_name())

