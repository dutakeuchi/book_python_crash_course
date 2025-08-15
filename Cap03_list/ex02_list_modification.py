# %%
names = []
names.append('Leila')
names.append("Dani")
names.append('Lele')
names
# %%
message = f'Would you like to dinner {names[0].title()}?'
print(message)
message = f'Would you like to dinner {names[1].title()}?'
print(message)
message = f'Would you like to dinner {names[2].title()}?'
print(message)
# %%
names_refused = []
refuse_name = names.pop(1)
names_refused.append(refuse_name)
names_refused
# %%
new_name = 'hayato'
names.append(new_name)
names
# %%
message = f'Would you like to dinner {names[0].title()}?'
print(message)
message = f'Would you like to dinner {names[1].title()}?'
print(message)
message = f'Would you like to dinner {names[2].title()}?'
print(message)
# %%
names.insert(0,'Paulo')
names.insert(2,'Dani')
names.append('midori')
names
# %%
print('I can invite only 2 people for the dinner')
names.pop()
names.pop()
names.pop()
names.pop()
names
# %%
del names[0]
del names[0]
names
# %%
