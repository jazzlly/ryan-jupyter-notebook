class Car:
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

class Battery:
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
    def __init__(self, make, model, year):
        super().__init__(make, model, year);
        self.battery = Battery()

    def describe_battery(self):
        self.battery.describe_battery()

    # 重载函数
    def fill_gas_tank(self):
        print('No gas tank for elactric car!')
