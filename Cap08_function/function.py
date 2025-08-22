# %%
def greet():
    print('Hello!')
# %%
def greet_user(name):
    print(f'Hello {name.title()}. Welcome to your python book')
# %%
def make_pizza(*args):
    print('We are making your pizza')
    for topping in args:
        print(topping)
# %%
