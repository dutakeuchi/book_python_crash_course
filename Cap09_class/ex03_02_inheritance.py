# %%
class Car:
    """simulating a car"""
    
    def __init__(self, make, model, year):
        """attributes from car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def info_car(self):
        """shows car information"""
        long_name = f'{self.year} {self.make.title()} {self.model.title()}'
        return long_name
    
    def read_odometer(self):
        """shows car milage"""
        return(f'This car has {self.odometer_reading}km on it')
    
    def update_odometer(self, milage):
        """update car milage"""
        if self.odometer_reading > milage:
            print("You can't roll back an odometer")
        elif self.odometer_reading <= milage:
            self.odometer_reading = milage
            
    def odometer_increment(self, milage):
        """increasce car milage"""
        self.odometer_reading += milage
        
class Battery:
    """battery from a eletric car model"""
    
    def __init__(self, battery_size = 40):
        """define battery size"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """describe battery from car"""
        return f'This car has a {self.battery_size}kWh battery'        
        
    def driving_range(self):
        """shows driving range car"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 60:
            range = 225
        elif self.battery_size == 100:
            range = 375
        return f'This car can drive for {range} miles'
        
class EletricCar(Car):
    """simulating an eletric car"""
    
    def __init__(self, make, model, year, battery_size = 40):
        """attributes from car"""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)
        
    
# %%
my_car = EletricCar('nissan','leaf', 2025, 100)
my_car.info_car()
# %%
my_car.battery.battery_size = 100
print(my_car.battery.describe_battery())
print(my_car.battery.driving_range())
# %%
my_car = EletricCar(make='nissan',model='leaf',year=2025,battery_size = 60)
# %%
