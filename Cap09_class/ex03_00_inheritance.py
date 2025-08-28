# %%
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
        """show if it's openor not"""
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
        
class IceCream(Restaurant):
    """create am ice cream store"""
    
    def __init__(self, name, cuisine, flavours):
        """start name, cuisine type and ice cream's flavours"""
        super().__init__(name, cuisine)
        
        if isinstance(flavours, list):
            self.flavours = []
            for flavour in flavours:
                self.flavours.append(flavour.title())

        else:
            self.flavours = [flavours]
        
    def add_flavour(self, flavour):
        """add flavours to our store"""
        if isinstance(flavour, list):
            for taste in flavour:
                if taste.title() not in self.flavours:
                    self.flavours.append(taste.title())
                else:
                    continue
        else:
            if flavour.title() not in self.flavours:
                self.flavours.append(flavour.title())
            else:
                return 'Flavour already in our list'
        
    def show_flavours(self):
        print('Our flavours')
        for flavour in self.flavours:
            print(flavour)
# %%
chic = IceCream('Chiquinho','Ice Cream','Vanilla')
print(chic.describe())
print(chic.flavours)
# %%
chic.add_flavour('chocolate')
print(chic.flavours)
print()
chic.add_flavour(['milk', 'oreo','chocolate','strawberry','lemon',
                  'chocolate'])
print(chic.flavours)
# %%
chic.show_flavours()
# %%
