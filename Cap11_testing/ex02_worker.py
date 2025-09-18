# %%
class Worker:
    '''get worker info'''
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary
        
    def show_info(self):
        name = f'{self.first_name} {self.last_name}'
        print(f'Name: {name}')
        print(f'Salary: {self.salary}')
        
    def increasce_salary(self, new_salary = 5000):
        self.salary += new_salary
