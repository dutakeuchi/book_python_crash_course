
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
        
class Privilege:
    """create privileges to an admin"""
    
    # def __init__(self, privileges=''):
    #     """create privileges"""
    #     self.privilege = []
    #     if isinstance(privileges, list):
    #         for privilege in privileges:
    #             self.privilege.append(privilege)
    #     else:
    #         self.privilege = privileges
            
    def __init__(self):
        """create privileges"""
        self.privilege = []          
        
    def add_privilege(self, privileges):
        if isinstance(privileges, list):
            for privilege in privileges:
                if privilege not in self.privilege:
                    self.privilege.append(privilege)
                else:
                    print(f'{privilege} is already in list')
        else:
            if privileges not in self.privilege:
                self.privilege.append(privileges)
            else:
                return f'{privileges} is already in list'
    
    def show_privileges(self):
        print("Admin privileges")
        for privilege in self.privilege:
            print(privilege)
        
class Admin(User):
    """create an admin"""
    
    def __init__(self, f_name, l_name, age, nacionality, blood):
        """create admin name, last name, age, nacionality and blood type"""
        super().__init__(f_name, l_name, age, nacionality, blood)
        self.privilege = Privilege()
        
    def info_user(self):
        """describe user"""
        full_name = f'{self.f_name.title()} {self.l_name.title()}'
        print(f'Full name: {full_name}')
        print(f'Age: {self.age}')
        print(f'Nacionality: {self.nacionality.lower()}')
        print(f'Blood type: {self.blood.upper()}')
        print(self.privilege.show_privileges())
        
# %%
adm = Admin('john','ken', 35, 'brazilian','a+')
adm.info_user()
# %%
adm.privilege.add_privilege(['add user','add post','edit post','delete post', 
                         'delete post'])
adm.privilege.show_privileges()
# %%
adm.info_user()
# %%
adm.privilege.add_privilege('add user')
adm.privilege.show_privileges()
# %%
