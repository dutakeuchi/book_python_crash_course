# %%
person = {}
person['name'] = 'john'
person['last_name'] = 'kennedy'
person['age'] = 35
person['city'] = 'New Jersey'
person
# %%
fav_numbers = {'john':10, 'anna':3, 'paul':45, 'carl':7, 'josh':12,}
for fav_number in fav_numbers:
    print(f"{fav_number.title()}'s favourite number is {fav_numbers[fav_number]}\n")
# %%
for key, value in fav_numbers.items():
    print(f"{key.title()}'s favourite number is {value}\n")
# %%
fav_numbers['maria'] = 11
fav_numbers['pedro'] = 4
fav_numbers['michelle'] = 5
fav_numbers['tim'] = 7

for key, value in fav_numbers.items():
    print(f"{key.title()}'s favourite number is {value}\n")
# %%
poll = ['john','albert','anna','pedro','hilda']

for name in sorted(poll):
    if name in fav_numbers:
        print(f'Thanks {name.title()} for join our poll\n')
    else:
        print(f'{name.title()}, please take our poll\n')
# %%
alien_0 = {'color': 'green', 'points': 5,}
alien_1 = {'color': 'yellow', 'points': 10,}
alien_2 = {'color': 'red', 'points': 15,}

aliens = [alien_0, alien_1, alien_2,]
aliens
# %%
aliens = []
for i in range(5):
    new_alien = {'color': 'green', 'points': 5,}
    aliens.append(new_alien)

aliens
# %%
for alien in aliens[:2]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 3

aliens
# %%
