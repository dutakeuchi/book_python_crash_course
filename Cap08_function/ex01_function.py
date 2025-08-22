# %%
def fav_book():
    book = input('Text your favorite book.')
    print(f'Your favorite book is {book.title()}')
    
fav_book()
 # %%
def my_pet(animal_type, name_pet):
    """function to write name's animal and type"""
    print(f'I have a {animal_type}')
    print(f"My {animal_type}'s name is {name_pet}")
# %%
my_pet('dog','harry')
# %%
my_pet('harry', 'dog')
# %%
my_pet(name_pet='harry', animal_type='dog')
# %%
def my_pet(name_pet, animal_type='dog'):
    """function to write name's animal and type"""
    print(f'I have a {animal_type}')
    print(f"My {animal_type}'s name is {name_pet}")
# %%
my_pet('harry')
# %%
my_pet('harry','hamster')
# %%
my_pet('hamster','harry')
# %%
my_pet('harry','cat','rabbit')
# %%
