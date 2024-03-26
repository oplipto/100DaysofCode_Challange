class Car:
    total_car = 0

    def __init__ (self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def full_Name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def Car_Description():
        return "This is a SuperCar"
    
    @property
    def car_model(self):
        return self.__model + "!"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"

myTesla = ElectricCar("Tesla", "Model S", 100)
# print(isinstance(myTesla, Car))
# print(isinstance(myTesla, ElectricCar))

# print(myTesla.full_Name())
# print(myTesla.battery_size)
# print(myTesla.get_brand())
# print(myTesla.fuel_type())
# print(myTesla.__brand)

# my_car = Car("Lamborghini", "Aventador")
# print(my_car.get_brand())
# print(my_car.fuel_type())
# print(Car.total_car)
# print(Car.Car_Description())
# print(my_car.car_model)

# myCar = Car("Toyota", "Corolla")
# print(myCar.brand)
# print(myCar.model)
# print(myCar.full_Name())

# myCar2 = Car("Honda", "Civic")
# print(myCar2.brand)
# print(myCar2.model)
# print(myCar2.full_Name())

class battery:
    def battery_info(self):
        return "This is battery"
    
class engine:
    def engine_info(self):
        return "This is engine"
    
class ElectricCar2(battery, engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())