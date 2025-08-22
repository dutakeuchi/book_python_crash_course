# %%
def formatted_name(f_name, l_name):
    full_name = f'{f_name.title()} {l_name.title()}'
    return full_name        
# %%
formatted_name('john','cash')
# %%
def format_name():
    
    while True:
        print("Tell me your name")
        f_name = input('Your first name')
        l_name = input('Your last name')
        full_name = f'{f_name.title()} {l_name.title()}'
        print(full_name)
# %%
format_name()
# %%
def format_name():
    
    while True:
        print("Tell me your name")
        print("Enter 'q' to exit program")
        
        f_name = input('Your first name')
        
        if f_name == 'q':
            break
        
        l_name = input('Your last name')
        
        if l_name == 'q':
            break
        
        full_name = f'{f_name.title()} {l_name.title()}\n'
        print(full_name)
# %%
format_name()
# %%
