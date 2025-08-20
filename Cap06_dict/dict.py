# %%
alien = {'color':'green','points':5}
alien['color']
# %%
alien['points']
# %%
print(f'The alien you killed is {alien['color']} and you got {alien['points']} points')
# %%
alien['color'] = 'yellow'
alien
# %%
alien['x_position'] = 0
alien['y_position'] = 25
alien['speed'] = 'medium'
alien
# %%
print(f'Original x position: {alien['x_position']}')

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
elif alien['speed'] == 'fast':
    x_increment = 3
    
alien['x_position'] = alien['x_position'] + x_increment

print(f'New x position: {alien['x_position']}') 
# %%
del alien['points']
# %%
alien
# %%
alien.get('points','No points value')
# %%
alien.get('points',10)
# %%
p = alien.get('points','No points value')
p
# %%
fav_numbers = {'john':10, 'anna':3, 'paul':45, 'carl':7, 'josh':12,}

for key, value in fav_numbers.items():
    print(f"{key.title()}'s favourite number is {value}\n")
# %%
for i in fav_numbers.items():
    print(i[0])
# %%
fav_numbers.keys()
# %%
sorted(fav_numbers.keys())
# %%
