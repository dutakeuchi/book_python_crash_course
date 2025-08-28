# %%
class Dog:
    """modeling a dog class"""
    def __init__(self, name, age):
        """start name and age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """simulates a dog sitting"""
        print(f'{self.name} is sitting now.')
        
    def roll_over(self):
        """simulates a dog rolling over"""
        print(f'{self.name} rolled over.')
# %%
my_dog = Dog('Willie',6)
# %%
my_dog.name
# %%
f'My dog {my_dog.name} has {my_dog.age} years'
# %%
my_dog.sit()
# %%
your_dog = Dog('Lili',15)
f'Your dog {your_dog.name} has {your_dog.age} years'
# %%
your_dog.sit()
# %%
