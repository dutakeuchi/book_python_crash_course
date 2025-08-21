# %%
car = input('Which car model would you like?')
print(f"I'm gonna check if we have {car.title()} available")
# %%
number_table = input('How many people would you like a table for?')
number_table = int(number_table)

if number_table >= 8:
    print(f'Please wait until we have table for {number_table} available.')
else:
    print('Please come with me.')
# %%
number = input('Digit any number.')
number = int(number)

if number % 10 == 0:
    print(f'{number} is multiple of 10')
else:
    print(f'{number} is not multiple of 10')
# %%
