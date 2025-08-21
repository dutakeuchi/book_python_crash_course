# %%
toppings = []
while True:
    topping = input('Choose your toppings. Text "quit" to exit')
    
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f'Adding {topping} to your pizza')

print()
print('Your pizza be will ready soon')
for top in toppings:
    print(top)
# %%
while True:
    age = input("What's your age?")
    
    if age == 'quit':
        break
    elif age != 'quit':
        age = int(age)
        if (age < 3):
            price = 0
        elif (age >= 3) and (age < 12):
            price = 10
        elif (age >= 12):
            price = 15
    
    print(f'You are {age}. Your ticket fee is {price}')
# %%
active = True
while active:
    age = input("What's your age?")
    
    if age == 'quit':
        active = False
    elif age != 'quit':
        age = int(age)
        if (age < 3):
            price = 0
        elif (age >= 3) and (age < 12):
            price = 10
        elif (age >= 12):
            price = 15
        print(f'You are {age}. Your ticket fee is {price}')
# %%
