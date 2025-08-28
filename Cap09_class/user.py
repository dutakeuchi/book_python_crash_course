"""class to create a user"""
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
        