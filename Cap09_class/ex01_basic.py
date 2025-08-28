# %%
class Restaurant:
    """create a restaurant"""
    def __init__(self, name, cuisine):
        """start name and cuisine type"""
        self.name = name
        self.cuisine = cuisine
        
    def describe(self):
        """General describe of the restaurant"""
        print(f'Our restaurant calls {self.name.title()} and we server {self.cuisine} food.')
        
    def open(self):
        """show if it's openor not"""
        print(f'{self.name} is open!')
# %%
rest = Restaurant("John's burger", "burger")

rest.describe()
rest.open()
# %%
rest1 = Restaurant("hokama", 'japanese')
rest2 = Restaurant("Pedrito", 'italian')

rest1.describe()
rest2.describe()
# %%
class User:
    
    def __init__(self, f_name, l_name, age, nacionality, blood):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.nacionality = nacionality
        self.blood = blood
        
    def info_user(self):
        full_name = f'{self.f_name.title()} {self.l_name.title()}'
        print(f'Full name: {full_name}')
        print(f'Age: {self.age}')
        print(f'Nacionality: {self.nacionality.lower()}')
        print(f'Blood type: {self.blood.upper()}')
        
    def greet_user(self):
        full_name = f'{self.f_name.title()} {self.l_name.title()}'
        return (f'Hello {full_name}')
# %%
user = User(blood='A+', age=30, f_name='John', l_name='kennedy',
            nacionality='Canadian')

print(user.info_user())
print(user.greet_user())
# %%
user.greet_user()
# %%
user.info_user()
# %%
user = User(blood='A+', age=30, f_name='John', l_name='kennedy',
            nacionality='Canadian')
user2 = User(blood='o-', age=18, f_name='carl', l_name='bush',
             nacionality='Russian')
user3 = User(blood='Ab+', age=65, f_name='anna', l_name='ozy',
             nacionality='german')

user.info_user()
user2.info_user()
user3.info_user()
# %%
