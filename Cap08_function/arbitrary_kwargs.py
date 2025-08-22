# %%
def full_name(first, last, **kwargs):
    kwargs['first_name'] = first.title()
    kwargs['last_name'] = last.title()
    return kwargs

full_name('john','cash')
# %%
full_name('john','cash',age=35)
# %%
full_name('john','cash',age = 35, city = 'Berlim', blood_type = 'A+')
# %%
