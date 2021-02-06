#%%
class Dog:
    # 添加下划线的方法是python默认方法
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name} sit')

    def roll(self):
        print(f'{self.name} roll')

dog = Dog('wuf', 3)
dog.sit()
dog.roll()

#%%
dog.name

#%%
dog.age

#%%
print(__name__)

#%%
class Car:
    '''类文档, blabla...'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.gas = 0
    
    def descriptive_name(self):
        return f'{self.make}, {self.model}, {self.year}'

    def update_odometer(self, odometer):
        self.odometer = odometer
    
    def fill_gas_tank(self):
        self.gas = 100

car = Car('audi', 'a4', 2010)
print(f'car: {car.descriptive_name()}')
print(f'car odometer: {car.odometer}')

#%% 直接修改属性
car.odometer = 23

#%%
car.update_odometer(28)
car

#%%
car.fill_gas_tank()
print(car.gas)

#%% 继承
class Battery:
    '''类文档, blabla...'''

    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f'battery: {self.battery_size}')

    def get_range(self):
        if self.battery_size == 75:
            return 260
        if self.battery_size == 100:
            return 315

class ElectricCar(Car):
    '''doc, blabla...'''

    def __init__(self, make, model, year):
        super().__init__(make, model, year);
        self.battery = Battery()

    def describe_battery(self):
        self.battery.describe_battery()

    # 重载函数
    def fill_gas_tank(self):
        print('No gas tank for elactric car!')

electric_car = ElectricCar('Tesla', 'Model Y', 2021)
print(f'ecar: {electric_car.descriptive_name()}')
electric_car.describe_battery()

#%% 方法重载
electric_car.fill_gas_tank()

#%% 
from car import Car, ElectricCar, Battery
from car import ElectricCar as Ecar

