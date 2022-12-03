# from module import class
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# 修改属性的2种方法
# 方法1：直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 方法2：通过方法修改属性的值
my_new_car.update_odometer(20)
my_new_car.read_odometer()
