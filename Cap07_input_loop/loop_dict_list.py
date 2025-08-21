# %%
unconfirmed_users = ['john','alice','anna']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Checking user: {current_user.title()}')
    confirmed_users.append(current_user)

print('\nUsers confirmed')
for user in confirmed_users:
    print(user.title())
# %%
unconfirmed_users = ['john','alice','anna','michael','paul']
confirmed_users = ['john','leo','anna','carlos']
users_now = []
users_denied = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    if current_user not in confirmed_users:
        print(f'Checking user: {current_user.title()}. Confirmed')
        confirmed_users.append(current_user)
        users_now.append(current_user)
    else:
        print(f'Checking user: {current_user.title()}. Denied')
        users_denied.append(current_user)

print('\nUsers confirmed')
for user in users_now:
    print(user.title())
    
print('\nUsers denied')
for user in users_denied:
    print(user.title())
# %%
responses = {}
flag = True

while flag:
    name = input('Your name:')
    car = input('Which car would you like to buy?')
    responses[name] = car
    
    answer = input('Does anyone would like to join? yes/no')
    answer = answer.lower()
    if answer == 'no':
        flag = False
    elif answer == 'yes':
        continue
    
for name, car in responses.items():
    print(f'{name.title()} would like to buy a {car.title()}')
# %%
