""" 一个可用于表示汽车的类 """
# 模块级文档字符串

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 里程数，提供默认值

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # 禁止将里程数回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        print("fill gas tank.")

    def increment_odomenter(self, miles):
        self.odometer_reading += miles
