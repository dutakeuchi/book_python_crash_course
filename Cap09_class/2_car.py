# %%
class Car:
    """simulating a car"""
    
    def __init__(self, make, model, year):
        """attributes from car"""
        self.make = make
        self.model = model
        self.year = year
        
    def info_car(self):
         long_name = f'{self.year} {self.make.title()} {self.model.title()}'
         return long_name
# %%
new_car = Car('Toyota','Etios',2024)
new_car.info_car()
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
# %%
new_car = Car('Toyota','Etios',2024)
print(new_car.info_car())
print(new_car.read_odometer())
# %%
new_car.odometer_reading = 50
print(new_car.read_odometer())
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
# %%  
new_car = Car('Toyota','Etios',2024)
print(new_car.info_car())
new_car.update_odometer(100)
print(new_car.read_odometer())
# %%
new_car.update_odometer(10)
print(new_car.read_odometer())
# %%
new_car.odometer_increment(15)
print(new_car.read_odometer())
# %%
