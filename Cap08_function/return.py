# %%
def formatted_name(first_name, last_name):
    full_name = f'{first_name.title()} {last_name.title()}'
    return full_name

name = formatted_name('john','obama')
print(name)
# %%
name
# %%
def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f'{first_name.title()} {middle_name.title()} {last_name.title()}'
    else:
        full_name = f'{first_name.title()} {last_name.title()}'
    return full_name
# %%
formatted_name('john','kenn')
# %%
formatted_name('carlos','viana','paul')
# %%
def formatted_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f'{first_name.title()} {middle_name.title()} {last_name.title()}'
    else:
        full_name = f'{first_name.title()} {last_name.title()}'
    return full_name
# %%
formatted_name('john','carlos','asdq')
# %%
def person_info(name, last_name, age):
    """get informations about someone"""
    person = {'name':name, 'last_name':last_name, 'age':age}
    return person
# %%
person = person_info('john','rock',27)
person
# %%
def person_info(name, last_name, age=None):
    """get informations about someone"""
    person = {'name':name, 'last_name':last_name, 'age':age}
    return person

person_info('john','rock')
# %%
person_info('john','rock', 27)
# %%
