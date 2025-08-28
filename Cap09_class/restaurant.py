# %%
"""modulo for create a new restaurant"""
class Restaurant:
    """create a restaurant"""
    
    def __init__(self, name, cuisine):
        """start name and cuisine type"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
        
    def describe(self):
        """General describe of the restaurant"""
        return(f'Our restaurant calls {self.name.title()} and we server {self.cuisine} food.')
        
    def open(self):
        """show if it's open or not"""
        return(f'{self.name.title()} is open!')
    
    def customers_served(self):
        return f"Today, we served {self.number_served} customers"
        
    def set_number_served(self, number):
        """set number of customers served"""
        if number >= self.number_served:
            self.number_served = number
        elif number < self.number_served:
            return f"You can't input less than {self.number_served}"
        
    def increase_number_served(self, number):
        """increase number of customers served"""
        self.number_served += number