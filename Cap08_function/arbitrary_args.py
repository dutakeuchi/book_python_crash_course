# %%
def make_pizza(*toppings):
    print('We are making your pizza with the following toppings:')
    for topping in toppings:
        for top in topping:
            print(top)
        
toppings = 'cheese','ham','bacon','pineapple'
make_pizza(toppings)
# %%
def make_pizza(*toppings):
    print(toppings)
    
make_pizza('cheese','ham','bacon','pineapple')
# %%
def make_pizza(*toppings):
    print('We are making your pizza with the following toppings:')
    for topping in toppings:
        print(topping)
        
toppings = ('cheese','ham','bacon','pineapple')
make_pizza(toppings)
# %%
def making_pizza(size, *arg):
    print(f'We are making a {size} pizza with the following toppings')
    for topping in arg:
        print(topping)
        
making_pizza('L','cheese','pepporoni','extra souce','chicken')
# %%
