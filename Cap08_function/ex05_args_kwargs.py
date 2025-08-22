# %%
def make_sandwich(*args):
    print('We are making your sandwich')
    for topping in args:
        print(topping)
    print()
        
make_sandwich('cheese','ham','tomato','lettuce')
make_sandwich('chesse','burguer','mostard')
make_sandwich('sausage','ketchup','mostard','tomato','corn')
# %%
def user_profile(first, last, **kwargs):
    kwargs['first_name'] = first.title()
    kwargs['last_name'] = last.title()
    return kwargs

user_profile('Eduardo','takeuchi', age=34, city='São Paulo', eyes='brown')
# %%
