# %%
"""class that can be used to represent a car"""
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