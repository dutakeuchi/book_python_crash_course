# %%
from name_function import get_formatted_name
# %%
print("Let's get your name")

while True:
    first_name = input('Digit your first name. Digit quit to stop')
    if first_name == 'q':
        break
    
    last_name = input('Digit your last name. Digit quit to stop')
    if last_name == 'q':
        break
    
    first_last_name = get_formatted_name(first_name, last_name)
    print (first_last_name)
# %%
get_formatted_name('john','obama')
# %%
get_formatted_name('john','obama','jesus')
# %%
