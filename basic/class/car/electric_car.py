from car import Car

class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


# 继承，父类名字写在子类的()中
class ElectricCar(Car):

    # 子类构造函数需要调用父类构造函数
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 将实例作为属性
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car don't need a gas tank.")
