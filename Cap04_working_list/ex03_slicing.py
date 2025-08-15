# %%
names = ['paul', 'john','anna','michel','marcus','jenn']
names
# %%
print('The first 3 elements are:')
for name in names[:3]:
    print(name.title())
# %%
print('The 4 middle elements are:')
for name in names[1:5]:
    print(name.title())
# %%
print('The last 3 elements are:')
for name in names[-3:]:
    print(name.title())
# %%
my_pizza = ['hawaiian','pepperoni','cheese']
friend_pizza = my_pizza[:]
# %%
print('My favorite pizzas are:')
for pizza in my_pizza:
    print(pizza)
    
print("\n")

print('My friend favorite pizzas are:')
for pizza in friend_pizza:
    print(pizza)
# %%
my_pizza.append('portuguese')
friend_pizza.append('chocolate')
# %%
print('My favorite pizzas are:')
for pizza in my_pizza:
    print(pizza)
    
print("\n")

print('My friend favorite pizzas are:')
for pizza in friend_pizza:
    print(pizza)
# %%
