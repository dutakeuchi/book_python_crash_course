# %%
names = ['Ed','john','admin','ANNA','Maria']

for name in names:
    if name.lower() == 'admin':
        print(f'Hello {name.title()}. Would you like to see the weekly report?')
    else:
        print(f'Hello {name.title()}. Welcome back.')
# %%
names = ['Ed','john','admin','ANNA','Maria']

if names:
    for name in names:
        if name.lower() == 'admin':
            print(f'Hello {name.title()}. Would you like to see the weekly report?')
        else:
            print(f'Hello {name.title()}. Welcome back.')
else:
    print('No username found')
# %%
names = []

if names:
    for name in names:
        if name.lower() == 'admin':
            print(f'Hello {name.title()}. Would you like to see the weekly report?')
        else:
            print(f'Hello {name.title()}. Welcome back.')
else:
    print('No username found')
# %%
current_users = ['ed','john','admin','anna','maria']

new_users = ['carlos','jeff','ed','josh','anna']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'{new_user.lower()} is already in use. Use another user.')
    else:
        print(f'User {new_user.lower()} available')
# %%
numbers = range(1,10)

for number in numbers:
    if number == 1:
        print(f'{number}st\n')
    elif number == 2:
        print(f'{number}nd\n')
    elif number == 3:
        print(f'{number}rd\n')
    else:
        print(f'{number}th\n')
# %%
