# %% 
languages = {
    'jenn':['python', 'c'],
    'anna':['go'],
    'john':['java','ruby'],
    'carl':['html','python','rust']   
    }

for name, language in languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for i in language:
        print(f'\t{i.title()}')
    print()
# %%
