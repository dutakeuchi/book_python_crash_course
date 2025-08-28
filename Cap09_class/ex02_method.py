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
# %%
rest = Restaurant('hokama','japanese')
print(rest.describe())
print(rest.open())
rest.set_number_served(10)
print(rest.customers_served())
# %%
rest.set_number_served(5)
# %%
rest.increase_number_served(35)
print(rest.customers_served())
# %%
class User:
    """create a user"""
    
    def __init__(self, f_name, l_name, age, nacionality, blood):
        """create user name, last name, age, nacionality and blood type"""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.nacionality = nacionality
        self.blood = blood
        self.login_attempts = 0
        
    def info_user(self):
        """describe user"""
        full_name = f'{self.f_name.title()} {self.l_name.title()}'
        print(f'Full name: {full_name}')
        print(f'Age: {self.age}')
        print(f'Nacionality: {self.nacionality.lower()}')
        print(f'Blood type: {self.blood.upper()}')
        
    def greet_user(self):
        """greet user"""
        full_name = f'{self.f_name.title()} {self.l_name.title()}'
        return (f'Hello {full_name}')
    
    def increment_login_attempt(self):
        """increment login attempt"""
        self.login_attempts += 1
        
    def reset_login(self):
        """reset login attempt"""
        self.login_attempts = 0
# %%
user = User(blood='A+', age=30, f_name='John', l_name='kennedy',
            nacionality='Canadian')

print(user.info_user())
print(user.greet_user())
print(f"Login attempt: {user.login_attempts}")
# %%
user.increment_login_attempt()
user.increment_login_attempt()
user.increment_login_attempt()
user.increment_login_attempt()
user.login_attempts
# %%
user.reset_login()
user.login_attempts
# %%
