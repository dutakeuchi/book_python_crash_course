# %%
message = input('Text anything and I will repeat it back')
print(message)
# %%
message = 'Share your name so we can personalize it.'
message += "\nWhat's your name?"

name = input(message)
print(f'Hello {name.title()}.')
# %%
age = input("Whats's your age? ")
age > 18
# %%
age = input("Whats's your age? ")
age = int(age)
age > 18
# %%
number = input('Digit a number')
number = int(number)

if number % 2 == 0:
    print(f'The number {number} is even')
elif number % 2 == 1:
    print(f'The number {number} is odd')
# %%
