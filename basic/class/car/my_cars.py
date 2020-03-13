# from car import Car, ElectricCar
import car
import electric_car

# my_beetle = Car('volkswagen', 'beetle', 2016)
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
