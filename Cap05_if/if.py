# %%
age = 19
if age >= 18:
    print('You are old enough to vote')
# %%
age = 16
if age >= 18:
    print('You are old enough to vote')
# %%
age = 19
if age >= 18:
    print('You are old enough to vote')
else:
    print("You can't vote yet")
# %%
age = 15
if age >= 18:
    print('You are old enough to vote')
else:
    print("You can't vote yet")
# %%
age = 19
if age < 4:
    print('Your ticket admission costs $0')
elif age < 18:
    print('Your ticket admission costs $25')
else:
    print('Your ticket admission costs $40')
# %%
age = 2
if age < 4:
    print('Your ticket admission costs $0')
elif age < 18:
    print('Your ticket admission costs $25')
else:
    print('Your ticket admission costs $40')
# %%
age = 15
if age < 4:
    print('Your ticket admission costs $0')
elif age < 18:
    print('Your ticket admission costs $25')
else:
    print('Your ticket admission costs $40')
# %%
age = 18
if age < 4:
    print('Your ticket admission costs $0')
elif age < 18:
    print('Your ticket admission costs $25')
else:
    print('Your ticket admission costs $40')
# %%
age = 4
if age < 4:
    print('Your ticket admission costs $0')
elif age < 18:
    print('Your ticket admission costs $25')
else:
    print('Your ticket admission costs $40')
# %%
age = 4
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
    
print(f'Your ticket admission costs ${price}')
# %%
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    
print(f'Your ticket admission costs ${price}')
# %%
toppings = ['cheese','pepperoni']

if 'cheese' in toppings:
    print('Add cheese')
if 'mushroom' in toppings:
    print('Add mushroom')
if 'pepperoni' in toppings:
    print('Add pepperoni')
print('\nFinishing your pizza')
# %%
toppings = ['cheese','pepperoni','green pepper']
for topping in toppings:
    print(f'Adding {topping}')
    
print('Finished making your pizza')
# %%
toppings = ['cheese','pepperoni','green pepper']
for topping in toppings:
    if topping == 'green pepper':
        print('Sorry, we are out of green pepper')
    else:
        print(f'Adding {topping}')
    
print('Finished making your pizza')
# %%
request_toppings = []
if request_toppings:
    for request_topping in request_toppings:
        print(f'Adding {request_topping}')
    print('Finished making your pizza')
else:
    print('Your pizza will be without topping')
# %%
available_toppings = ['cheese','pepperoni','pineapple','meat','green pepper',
                      'mushroom','sausage','ham']

request_toppings = ['cheese','french fries','pineapple']

if request_toppings:
    for request_topping in request_toppings:
        if request_topping in available_toppings:
            print(f'Adding {request_topping}')
        else:
            print(f'Sorry, we are out of {request_topping}')
    print('\nFinished making your pizza')
    
else:
    print('Your pizza will be without topping')
# %%
available_toppings = ['cheese','pepperoni','pineapple','meat','green pepper',
                      'mushroom','sausage','ham']

request_toppings = ['cheese','sausage','pineapple']

if request_toppings:
    for request_topping in request_toppings:
        if request_topping in available_toppings:
            print(f'Adding {request_topping}')
        else:
            print(f'Sorry, we are out of {request_topping}')
    print('\nFinished making your pizza')
    
else:
    print('Your pizza will be without topping')
# %%
